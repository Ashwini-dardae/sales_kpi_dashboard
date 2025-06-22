
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent
import os

os.environ["GROQ_API_KEY"] = "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"

def get_llm():
    return ChatGroq(temperature=0, model_name="llama3-70b-8192")

def ask_question(df, query):
   agent = create_pandas_dataframe_agent(get_llm(), df, verbose=False, allow_dangerous_code=True)
   return agent.run(query)
    

def get_summary(df):
    prompt = f"Summarize this sales data in simple terms: {df.head(10).to_string()}"
    return get_llm().invoke(prompt).content
