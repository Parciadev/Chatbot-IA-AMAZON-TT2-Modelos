# Importar OS, Bedrock, ConversationChain, ConversationBufferMemory Langchain Modules

import os
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Funcion para invocar el modelo - conexion al cliente de bedrock con el perfil, model_id & inference params-

def demo_chatbot(imput_text):
    demo_llm = Bedrock(
        credentials_profile_name= 'default',
        model_id='ai21.j2-ultra-v1', # Importante
        model_kwargs= {
            "temperature": 0.9,
            "top_p": 0.5,
            "max_gen_len": 512
        }
    )
    #return demo_llm

# Probando LLM con un modelo de prediccion
    return demo_llm.invoke(imput_text)

response = demo_chatbot('hola, cual es tu nombre?')
print(response)
