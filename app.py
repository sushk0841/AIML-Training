import gradio as gr
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import json

# Initialize the model and parser
model = ChatOllama(
    model="llama3.2",
    temperature=0.25,
    base_url="https://alpaca-upright-vulture.ngrok-free.app"
)

parser = JsonOutputParser()
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | model | parser

def generate_recipe_json(query):
    try:
        results = chain.invoke({"query": query})
        # Format JSON with indentation for better readability
        formatted_json = json.dumps(results, indent=2)
        return formatted_json
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio interface
with gr.Blocks(title="Recipe JSON Generator") as demo:
    gr.Markdown("# 🍳 Recipe JSON Generator")
    gr.Markdown("Get recipe information in JSON format!")
    
    with gr.Row():
        query_input = gr.Textbox(
            label="Your Query",
            placeholder="Enter your recipe query...",
            value="how to make gulab jam with ingredients"
        )
    
    generate_btn = gr.Button("Generate Recipe JSON")
    
    json_output = gr.Code(
        label="Recipe JSON",
        language="json",
    )
    
    generate_btn.click(
        fn=generate_recipe_json,
        inputs=[query_input],
        outputs=[json_output]
    )

# Launch the interface
if __name__ == "__main__":
    demo.launch()