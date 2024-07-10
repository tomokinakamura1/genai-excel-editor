from ibm_watson_machine_learning.foundation_models import Model
import pandas as pd
import os
from dotenv import load_dotenv
from app.prompts import v1
import json
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
    # Extract the JSON part from the input
    json_start = output.find('{')
    json_end = output.rfind('}') + 1
    json_str = output[json_start:json_end].strip()

    # Convert JSON string to Python dictionary
    data_dict = json.loads(json_str)

    # Extract the 'equipment_info' list from the dictionary
    equipment_info = data_dict['equipment_info']

    # Create DataFrame from the list of dictionaries
    df = pd.DataFrame(equipment_info)
    return df


def read_table(file_path):
    df=pd.read_csv(file_path)
    return df


def extract_entity(prompt,column_output,input_table):
    # df = read_table(file_path)
    df=column_output
    output=entity(prompt,df)
    output_df=convert_to_df(output)
    final_df=pd.concat([input_table, output_df], axis=1)
    return output,final_df


def extract_entity_line_by_line(input_prompt,file_path):
    df=file_path
    # output=entity(input_prompt,df)
    final_response=[]
    for index, row in df.iterrows():
        prompt = append_question(
            input_prompt=input_prompt,
            df=row
        )
        response=model.generate(prompt)
        intermediate_respoonse=response.get("results")[0].get("generated_text")[:-5]
        # print(response)
        print(intermediate_respoonse)
        final_response.append(intermediate_respoonse)
        yield final_response
    
    

# Function to extract JSON content
def extract_json_from_string(json_str):
    match = re.search(r'{.*}', json_str, re.DOTALL)
    if match:
        return match.group(0)
    return None

def get_table(final_response,file_path):
    print(final_response)
    combined_json = []

    for json_str in final_response:
        json_content = extract_json_from_string(json_str)
        if json_content:
            json_obj = json.loads(json_content)
            combined_json.append(json_obj)

    combined_json_str = json.dumps(combined_json, indent=2, ensure_ascii=False)
    df=convert_to_df(combined_json_str)
    final_df=pd.concat([file_path, df], axis=1)
    return final_df