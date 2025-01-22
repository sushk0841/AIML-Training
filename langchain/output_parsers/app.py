from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

ollama_base_url=os.getenv("OLLAMA_BASE_URL")
model=OllamaLLM(model="llama3.2",temperature=0.25,base_url=ollama_base_url)

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



# Using pydantic classes
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from pydantic import BaseModel,Field
import json

class world(BaseModel):
    continents: str=Field(description="name of the continents")
    oceans: str=Field(description="name of the oceans")

parser=JsonOutputParser(pydantic_object=world)

query="name the 7 continents and 5 oceans"
llm=OllamaLLM(model="llama3.2",temperature=0.2, base_url="https://dev-ollama.huhoka.com")

prompt=PromptTemplate(
    template="answer the following {query}\n{format_instructions}",
    input_variables=["query"],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

chain= prompt | llm | parser

results=chain.invoke({query})

print(results)