import os
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def demo_chatbot():
    demo_llm = Bedrock(
        credentials_profile_name='default',
        model_id = 'anthropic.claude-v2:1',
        model_kwargs= {
            "max_tokens_to_sample": 300,
            "temperature": 0.5,
            "top_p": 0.9
        }
    )
    return demo_llm

def demo_memory():
    llm_data = demo_chatbot
    memory = ConversationBufferMemory(llm=llm_data, max_token_limit=256)
    return memory

def demo_conversation(input_text,memory):
    llm_chain_data = demo_chatbot()
    llm_conversation = ConversationChain(llm=llm_chain_data,memory=memory,verbose=True)

    chat_reply = llm_conversation.predict(input=input_text)
    return chat_reply