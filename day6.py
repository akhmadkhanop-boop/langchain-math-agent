from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
import os

load_dotenv()

@tool
def check_even_odd(number: int) -> str:
    """Tells whether a number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."
    
@tool
def check_prime(number: int) -> str:
    """Tells whether a number is prime or not."""
    if number < 2:
        return f"{number} is not prime."
    for i in range(2, number):
        if number % i == 0:
            return f"{number} is not prime."
    return f"{number} is prime."
     
@tool
def generate_table(number: int) -> str:
    """Generates the multiplication table for a number (from 1 to 10)."""
    table = ""
    for i in range(1, 11):
        table += f"{number} x {i} = {number * i}\n"
    return table
         
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

agent = create_agent(llm, [check_even_odd, check_prime, generate_table])

question = "Is 8 a prime number?"

result = agent.invoke({"messages": [("user", question)]})

print("FINAL ANSWER:")
print(result["messages"][-1].content)