from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

file_path=(r"C:\Users\SushantKulkarni\Documents\AIML Training\docs\aditya_mehetre_resume.pdf")

loader=PyPDFLoader(file_path)
# you can use different loaders like PyPDFLoader, DocxLoader, TextLoader, etc.
data=loader.load()

# print(data)

splitter= CharacterTextSplitter(chunk_size=100,chunk_overlap=100)

chunks=splitter.split_documents(data)

print(chunks[0])