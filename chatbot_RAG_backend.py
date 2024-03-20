import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter  import RecursiveCharacterTextSplitter
from langchain.llms.bedrock import Bedrock
from langchain.embeddings import BedrockEmbeddings
from langchain.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

#Carga de PDF
def hr_index():
    data_load=PyPDFLoader('https://biblioteca.utem.cl/wp-content/uploads/2018/01/Reglamento-Gral.-Estudiantes-1.pdf')
    data_split=RecursiveCharacterTextSplitter(separators=["\n\n","\n"," ",""], chunk_size=100,chunk_overlap=10)
    data_embeddings=BedrockEmbeddings(
        credentials_profile_name='default',
        model_id='amazon.titan-text-express-v1')

    data_index=VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding=data_embeddings,
        vectorstore_cls=FAISS)

    db_index=data_index.from_loaders([data_load])
    return db_index

#Carga del bot y tockens
def demo_chatbot():
    demo_llm = Bedrock(
        credentials_profile_name='default',
        model_id = 'anthropic.claude-v2',
        model_kwargs= {
            "max_tokens_to_samplle":1000,
            "temperature":0.1,
            "top_p":0.9,})
    return demo_llm
    #return demo_llm.invoke(input_text)
    #response = demo_chatbot('Hola, dime cual es tu nombre?')
    #print(response)

#Carga inicial de texto
def demo_memory():
    llm_data = demo_chatbot
    memory = ConversationBufferMemory(llm=llm_data, max_token_limit=256)
    return memory

#Continuacion del texto
def demo_conversation(input_text,memory):
    llm_chain_data = demo_chatbot()
    llm_conversation = ConversationChain(llm=llm_chain_data,memory=memory,verbose=True)
    chat_reply = llm_conversation.predict(input=input_text)
   # RAG_llm=demo_chatbot()
   # RAG_pregunta=memory.query(memory=memory,llm=RAG_llm)
    return chat_reply
