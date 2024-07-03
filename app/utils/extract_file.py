from ibm_watson_machine_learning.foundation_models import Model
import pandas as pd
import os
from dotenv import load_dotenv
from app.prompts import v1
import re

load_dotenv()


def get_credentials():
    return {"url": os.getenv("IBM_CLOUD_URL"), "apikey": os.getenv("IBM_CLOUD_API_KEY")}


parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 2000,
    "min_new_tokens": 1,
    "stop_sequences": ["<end>"],
}


def create_model():
    model = Model(
        model_id="meta-llama/llama-3-70b-instruct",
        params=parameters,
        credentials=get_credentials(),
        project_id=os.getenv("PROJECT_ID"),
    )
    return model


model = create_model()


# search_item = ["Internal Pre-Sales Engagement", "Close-out and transition details"]
# metadata_info = ["internal_pre_sales_data_info", "close_out_transition_info"]


# def generate_prompt_answer(
#     question_data_dict, data_dict, metadata_info, search, output_dict
# ):
#     prompt = append_question(
#         question=question_data_dict,
#         user_input_metadata=data_dict,
#         table_metadata=input_metadata_question,
#         meta_data_info=metadata_info,
#     )
#     response = model.generate(prompt)
#     cleaned_response = clean_response(response, output_dict, search)
#     return cleaned_response


# def clean_response(generated_response, output_dict, search):
#     clean_data = generated_response.get("results")[0].get("generated_text")[:-5]
#     smart_data = json.loads(clean_data)
#     output_dict[search] = dict()
#     for key in smart_data:
#         output_dict[search][smart_data.get(key).get("content_key")] = smart_data.get(
#             key
#         ).get("content_value")
#     return output_dict


# def extract_data(df):
#     data_dict = dict()
#     output_dict = dict()
#     question_data_dict = dict()
#     data = []
#     for index, row in df.iterrows():
#         data_dict[row["key"]] = row["value"]

#     for i, search in enumerate(search_item):
#         df_question = stars_data[stars_data["Table"] == search]
#         for item in df_question["Information / Question"]:
#             question_data_dict[item] = " "
#         response = generate_prompt_answer(
#             question_data_dict, data_dict, metadata_info[i], search, output_dict
#         )
#         question_data_dict = dict()
#     return response


# def structure_response(data):
#     table_names = []
#     column_categories = []
#     column_values = []

#     for table_name, content in data.items():
#         for category, value in content.items():
#             table_names.append(table_name)
#             column_categories.append(category)
#             column_values.append(value)

#     df = pd.DataFrame(
#         {
#             "Table Name": table_names,
#             "Column Category": column_categories,
#             "Generated Text ": column_values,
#         }
#     )
#     return df


# def extract_table_from_slides(slide):
#     i = 0
#     data = {}
#     for i, shape in enumerate(slide.shapes):
#         i += 1
#         if shape.has_table:
#             table = shape.table
#             rows = []
#             for i, row in enumerate(table.rows):
#                 row_data = [cell.text.strip() for cell in row.cells]
#                 rows.append(row_data)
#             df_table = pd.DataFrame(rows, columns=["key", "value"])
#             tables = data.get("tables", [])
#             tables.append(df_table)
#             data["tables"] = tables
#         elif hasattr(shape, "text") and not shape.text.isspace() and shape.text != "":
#             if len(shape.text_frame.paragraphs) > 1:
#                 paragraphs = data.get("paragraphs", [])
#                 for i, paragraph in enumerate(shape.text_frame.paragraphs):
#                     if paragraph.text != "":
#                         paragraphs.append(paragraph.text)
#                 data["paragraphs"] = paragraphs
#             else:
#                 text_box = data.get("text_box", [])
#                 text_box.append(shape.text)
#                 data["text_box"] = text_box
#     data = extract_data(data["tables"][0])

#     res = structure_response(data)
#     return res


# def total_pipeline_process(file_path):
#     text_content = ""
#     ppt = Presentation(file_path)
#     slide = ppt.slides[0]
#     res = extract_table_from_slides(slide)
#     return res


def append_question(input_prompt,df):
    return v1.prompt_template.format(
        input_prompt=input_prompt,
        df=df
    )
def entity(input_prompt,df):
    prompt = append_question(
        input_prompt=input_prompt,
        df=df
    )
    response=model.generate(prompt)
    final_response=response.get("results")[0].get("generated_text")[:-5]
    print(response)
    print(final_response)
    return final_response

def convert_to_df(output):
    # Extract the lines containing the data
    data_section = output.split("Here is the output dataframe with the requested information:")[1].strip()
    lines = data_section.split('\n')

    # Initialize variables
    header = None
    data = []

    # Process each line
    for line in lines:
        # Use regex to split by one or more spaces outside of quotes
        values = re.split(r'\s+(?=(?:[^"]*"[^"]*")*[^"]*$)', line.strip())
        values = [v.strip('"') for v in values]  # Remove quotes around values
        if header is None:
            header = values
        else:
            data.append(values)

    # Create a DataFrame
    df = pd.DataFrame(data, columns=header)
    return df


def read_table(file_path):
    df=pd.read_csv(file_path)
    return df


def extract_entity(input_prompt,file_path):
    df = read_table(file_path)
    output=entity(input_prompt,df)
    output_table=convert_to_df(output)
    return output,output_table