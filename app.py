import torch
import gradio as gr

# Use a pipeline as a high-level helper
from transformers import pipeline


question_answer = pipeline("question-answering",
                           model="deepset/roberta-base-squad2")

# question_answer = pipeline("question-answering",
#                            model=model_path)

def read_file_content(file_obj):
    """
    Reads the content of a file object and returns it.
    Parameters:
    file_obj (file object): The file object to read from.
    Returns:
    str: The content of the file.
    """
    try:
        with open(file_obj.name, 'r', encoding='utf-8') as file:
            context = file.read()
            return context
    except Exception as e:
        return f"An error occurred: {e}"




def get_answer(file, question):
    context = read_file_content(file)
    answer = question_answer(question=question, context=context)
    return answer["answer"]

demo = gr.Interface(fn=get_answer,
                    inputs=[gr.File(label="Upload your file"), gr.Textbox(label="Input your question",lines=1)],
                    outputs=[gr.Textbox(label="Answer text",lines=1)],
                    title="Document Q & A",
                    description="THIS APPLICATION WILL BE USED TO ANSER QUESTIONS BASED ON CONTEXT PROVIDED.")

demo.launch()