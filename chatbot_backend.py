import os
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def demo_chatbot(input_text):
    demo_llm = Bedrock(
        credentials_profile_name='default',
        model_id = 'meta.llama2-70b-chat-v1',
        model_kwargs= {
            "temperature": 0.9,
            "top_p": 0.5,
            "max_gen_len": 256
        }
    )
    #return demo_llm
    return demo_llm.invoke(input_text)
response = demo_chatbot('Hola, cual es el clima de santiago de hoy')
print(response)
