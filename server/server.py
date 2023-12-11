import os
from langchain import PromptTemplate, HuggingFaceHub, LLMChain


from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.llms.huggingface_hub import HuggingFaceHub

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatAnthropic, ChatOpenAI
from langserve import add_routes

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}

embedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)


print("Loading vector database...")

vectordb = Chroma(persist_directory='db',
                  embedding_function=embedding)






def retrieval_qa_chain(db, return_source_documents):
    llm = HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct", model_kwargs={"temperature": 0.6, "max_length": 500, "max_new_tokens": 700})
    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                           chain_type='stuff',
                                           retriever=db,
                                           return_source_documents=return_source_documents,
                                           )
    return qa_chain


db = vectordb.as_retriever(search_kwargs={'k': 3})
bot = retrieval_qa_chain(db,True)

res = bot("Asas nedir?")
print(res['result'])
print("#"*100)
for doc in res['source_documents']:
    print(doc.page_content)
    print("#"*100)


# app = FastAPI(
#   title="LangChain Server",
#   version="1.0",
#   description="A simple api server using Langchain's Runnable interfaces",
# )

# add_routes(
#     app,
#     ChatOpenAI(),
#     path="/openai",
# )

# add_routes(
#     app,
#     ChatAnthropic(),
#     path="/anthropic",
# )

# model = ChatAnthropic()
# prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
# add_routes(
#     app,
#     prompt | model,
#     path="/joke",
# )

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="localhost", port=8000)

# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = PromptTemplate(template=template, input_variables=["question"])
# llm_chain = LLMChain(prompt=prompt, 
#                      llm=HuggingFaceHub(repo_id="google/flan-t5-xl", 
#                                         model_kwargs={"temperature":0, 
#                                                       "max_length":64}))

# question = "What is the capital of England?"

# print(llm_chain.run(question))