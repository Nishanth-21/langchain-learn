import os
from langchain.chat_models import init_chat_model

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

model = init_chat_model(model="qwen/qwen3-32b",model_provider = "Groq")
for chunk in model.stream("what is cloud made of?"):
    print(chunk.text, flush=True)

    