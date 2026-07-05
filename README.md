# LangChain Math Agent 🤖📐

An autonomous AI agent built using **LangChain** and **Groq (Llama 3.3)**. This agent uses custom Python tools to understand natural language questions and perform mathematical operations dynamically.

## 🚀 Features (Tools)
The agent is equipped with the following custom tools:
1. **`check_even_odd`**: Determines whether a given integer is even or odd.
2. **`check_prime`**: Checks if a given number is a prime number.
3. **`generate_table`**: Generates a complete multiplication table (1 to 10) for any given number.

## 🛠️ Tech Stack
* **Language:** Python
* **Framework:** LangChain
* **LLM:** Llama-3.3-70b-versatile (via Groq API)
* **Environment:** python-dotenv

## ⚙️ Setup & Installation

**1. Install required libraries**
```bash
pip install langchain langchain-groq python-dotenv
