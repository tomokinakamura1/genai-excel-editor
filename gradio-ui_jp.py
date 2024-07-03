import gradio as gr
import pandas as pd
import os
from app.template.css import CUSTOM_CSS
from app.utils import extract_file

BANNER_PATH = os.path.join(os.getcwd(), "app/images/banner.jpg")

def analyze_file(file):
    df = pd.read_csv(file.name)
    return df

def download_content(df):
    df.to_csv('output.csv', index=False)
    return 'output.csv'


with gr.Blocks(theme=gr.themes.Soft(), css=CUSTOM_CSS) as demo:
    gr.Image(BANNER_PATH, show_label=False)
    
    ##heading###
    gr.Markdown(
        "<center><span style='font-size: 26px; font-weight: bold;'>Entity extractor</span></center>") 
    
    ###input file #####
    file_upload = gr.File(label="入力CSVをアップロード")
    review_button = gr.Button("総説", elem_id="custom-button1-id",
                                       elem_classes=["custom-button1-class"])
    
    input_table = gr.DataFrame(headers=None)

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
    
    extract_entity.click(extract_file.extract_entity, inputs=[prompt,file_upload], outputs=[output,output_table])

    ####Download Utils ####
    download_button = gr.Button("ダウンロード", elem_id="custom-button1-id",
                                       elem_classes=["custom-button1-class"])    
    
    download_button.click(download_content, inputs=output_table, outputs=gr.File())


demo.launch(server_port=8080)