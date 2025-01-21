from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

ollama_base_url=os.getenv("OLLAMA_BASE_URL")
model=ChatOllama(model="llama3.2",temperature=0.25,base_url=ollama_base_url)

joke_query = "how to make gulab jam with ingredients"

parser = JsonOutputParser()

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | model | parser

results=chain.invoke({"query": joke_query})
print(results)