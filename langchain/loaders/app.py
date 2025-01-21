from langchain_community.document_loaders import PyPDFLoader

file_path=()

loader=PyPDFLoader(file_path)
# you can use different loaders like PyPDFLoader, DocxLoader, TextLoader, etc.
data=loader.load()

print(data)