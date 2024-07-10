import gradio as gr
import pandas as pd
import os
from app_jp.template.css import CUSTOM_CSS
from app_jp.utils import extract_file

BANNER_PATH = os.path.join(os.getcwd(), "app/images/banner.jpg")

def analyze_file(file):
    df = pd.read_csv(file.name)
    return df

def download_content(df):
    df.to_csv('output.csv', index=False)
    return 'output.csv'

def display_column(file, column):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file.name)
    
    # Return the DataFrame and the selected column
    if column:
        return df, df[[column]]
    else:
        return df, None

def get_column_names(file):
    df = pd.read_csv(file.name)
    return list(df.columns)

with gr.Blocks(theme=gr.themes.Soft(), css=CUSTOM_CSS) as demo:
    gr.Image(BANNER_PATH, show_label=False)
    
    with gr.Tab("Full processor"):
        ##Header###
        gr.Markdown(
            "<center><span style='font-size: 26px; font-weight: bold;'>Entity extractor</span></center>") 
        
        ###input file#####
        file_upload = gr.File(label="入力CSVをアップロード")
        column_dropdown = gr.Dropdown(label="Select a column to display", choices=[], interactive=True)
        input_table = gr.DataFrame(headers=None)

        column_output = gr.DataFrame(label="Selected Column")
        review_button = gr.Button("総説", elem_id="custom-button1-id",
                                        elem_classes=["custom-button1-class"])
        
        file_upload.change(fn=lambda file: gr.update(choices=get_column_names(file)), inputs=file_upload, outputs=column_dropdown)

        
        review_button.click(fn=display_column, inputs=[file_upload, column_dropdown], outputs=[input_table, column_output])

        ####Entity extraction#######
        prompt=gr.TextArea(label="入力プロンプト",placeholder="please add underscore instead of spaces in column names")

        
        extract_entity = gr.Button("抽出する", elem_id="custom-button1-id",
                                        elem_classes=["custom-button1-class"])
        
        gr.Markdown(
            "<left><span style='font-size: 26px; font-weight: bold;'>生成された出力</span></left>")
        
        output=gr.TextArea(label="生成された出力")
        
        output_table=gr.DataFrame(headers=None)
        
        ###Button operations ####
        
        review_button.click(extract_file.read_table, inputs=file_upload, outputs=input_table)
        
        extract_entity.click(extract_file.extract_entity, inputs=[prompt,column_output,input_table], outputs=[output,output_table])

        ####Download Utils ####
        download_button = gr.Button("ダウンロード", elem_id="custom-button1-id",
                                        elem_classes=["custom-button1-class"])    
        
        download_button.click(download_content, inputs=output_table, outputs=gr.File())

    with gr.Tab("Line by line processor"):
        ##Header###
        gr.Markdown(
            "<center><span style='font-size: 26px; font-weight: bold;'>Entity extractor</span></center>") 
        
        ###input file#####
        file_upload = gr.File(label="入力CSVをアップロード")
        column_dropdown = gr.Dropdown(label="Select a column to display", choices=[], interactive=True)
        input_table = gr.DataFrame(headers=None)

        column_output = gr.DataFrame(label="Selected Column")
        review_button = gr.Button("総説", elem_id="custom-button1-id",
                                        elem_classes=["custom-button1-class"])
        
        file_upload.change(fn=lambda file: gr.update(choices=get_column_names(file)), inputs=file_upload, outputs=column_dropdown)

        
        review_button.click(fn=display_column, inputs=[file_upload, column_dropdown], outputs=[input_table, column_output])

        ####Entity extraction#######
        prompt=gr.TextArea(label="入力プロンプト",placeholder="please add underscore instead of spaces in column names")

        
        extract_entity = gr.Button("抽出する", elem_id="custom-button1-id",
                                        elem_classes=["custom-button1-class"])
        
        gr.Markdown(
            "<left><span style='font-size: 26px; font-weight: bold;'>生成された出力</span></left>")
        
        output=gr.TextArea(label="生成された出力")
        
        get_dataframe=gr.Button("get_dataframe", elem_id="custom-button",elem_classes=["custom-button1-class"])
        
        output_table=gr.DataFrame(headers=None)
        
        ###Button operations ####
        
        review_button.click(extract_file.read_table, inputs=file_upload, outputs=input_table)
        
        extract_entity.click(extract_file.extract_entity_line_by_line, inputs=[prompt,column_output], outputs=output)

        get_dataframe.click(extract_file.get_table, inputs=[output,file_upload], outputs=output_table)
        ####Download Utils ####
        download_button = gr.Button("ダウンロード", elem_id="custom-button1-id",
                                        elem_classes=["custom-button1-class"])    
        
        download_button.click(download_content, inputs=output_table, outputs=gr.File())

demo.launch(server_port=8080)