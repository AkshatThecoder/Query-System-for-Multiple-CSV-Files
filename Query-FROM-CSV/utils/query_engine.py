# import pandas as pd
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from utils.groq_llm import get_groq_llm

# def generate_query_prompt():
#     """Creates a LangChain prompt template for querying CSV data."""
#     return PromptTemplate(
#         input_variables=["schema", "question"],
#         template="Given the CSV schema:\n{schema}\n\nAnswer the question:\n{question}"
#     )

# def process_query(df, question):
#     """Processes a user query and returns a response using Groq API."""
#     llm = get_groq_llm()
#     chain = LLMChain(llm=llm, prompt=generate_query_prompt())

#     # Extract schema information
#     schema_info = f"Columns: {', '.join(df.columns)} | Rows: {len(df)}"

#     # Generate LLM response
#     response = chain.run({"schema": schema_info, "question": question})
    
#     return response






import pandas as pd
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.groq_llm import get_groq_llm
from langchain.schema.runnable import RunnableLambda
import re
import matplotlib.pyplot as plt
import streamlit as st  # 📌 Import Streamlit if not already imported

def generate_query_prompt():
    """Creates a LangChain prompt template for querying CSV data."""
    return PromptTemplate(
        input_variables=["schema", "question"],
        template=(
            "You have a pandas DataFrame named `df` with the following schema:\n"
            "{schema}\n\n"
            "Generate ONLY a valid Python pandas command to answer the following question:\n"
            "{question}\n"
            "Output ONLY the executable command. Do NOT include explanations, comments, or markdown formatting."
        )
    )


def process_query(df, question):
    """Processes a user query and executes the generated Pandas command."""
    llm = get_groq_llm()
    
    # Define the prompt
    def generate_query_prompt():
        return PromptTemplate(
            input_variables=["schema", "question"],
            template=(
                "You have a pandas DataFrame named `df` with the following schema:\n"
                "{schema}\n\n"
                "Generate ONLY a valid Python pandas command to answer the following question:\n"
                "{question}\n"
                "Output ONLY the executable command. Do NOT include explanations, comments, or markdown formatting."
            )
        )

    # Extract schema info
    schema_info = f"Columns: {', '.join(df.columns)} | Rows: {len(df)}"

    # Use RunnableLambda for better execution
    prompt = generate_query_prompt()
    chain = prompt | llm | RunnableLambda(lambda x: x.content if hasattr(x, "content") else str(x))

    # Generate the Pandas command
    pandas_command = chain.invoke({"schema": schema_info, "question": question}).strip()

    # 🔧 Fix: Remove backticks if they exist
    pandas_command = pandas_command.strip("`")

    # 🔍 Debugging: Show raw output before execution
    print(f"🔍 Raw Generated Command:\n{repr(pandas_command)}")

    # Ensure it's a clean Python statement
    pandas_command = re.sub(r"[^\x00-\x7F]+", "", pandas_command)  # Remove non-ASCII chars

    try:
        # Execute the command safely
        # result = eval(pandas_command, {"df": df, "pd": pd})  # Limit execution scope
        # return result
    
        if "plt" in pandas_command or "hist"    in pandas_command:
            fig, ax = plt.subplots()
            exec(pandas_command, {"df": df, "pd": pd, "plt": plt, "ax": ax})
            st.pyplot(fig)  # ✅ Display the plot in Streamlit
            return "📊 Histogram displayed successfully."
        else:
            result = eval(pandas_command, {"df": df, "pd": pd})
            return result
    except Exception as e:
        return f"❌ Error executing query: {e}"

