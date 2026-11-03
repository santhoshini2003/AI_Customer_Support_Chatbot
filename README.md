\# AI Customer Support Chatbot



An AI-powered customer support chatbot developed using Python and Google's Gemini API. This project generates responses to customer queries and includes response validation, automated testing, and AI response evaluation using Langfuse.



\## Project Overview



The AI Customer Support Chatbot is designed to assist users by providing relevant responses to customer queries. It uses a Large Language Model (LLM) to generate answers and applies validation techniques to improve response quality and safety.



The project also includes automated evaluation workflows to assess chatbot responses.



\## Key Features



\- AI-powered customer support response generation

\- Google Gemini API integration

\- Prompt engineering for better responses

\- Response validation and safety checks

\- Handling of inappropriate and out-of-scope queries

\- Prompt injection resistance testing

\- Hallucination and unknown-answer handling

\- Automated test case execution

\- Mock-based response evaluation

\- Langfuse integration for AI evaluation tracking



\## Technologies Used



| Technology | Purpose |

|---|---|

| Python | Core development |

| Google Gemini API | AI response generation |

| Streamlit | Chatbot interface |

| Langfuse | LLM monitoring and evaluation |

| Python-dotenv | Environment variable management |



\## Project Structure



```text

AI\_Customer\_Support\_Chatbot/

│

├── app/

│   ├── chatbot.py

│   ├── config.py

│   ├── llm\_client.py

│   ├── prompts.py

│   ├── ui.py

│   └── validators.py

│

├── data/

│

├── evaluation/

│   ├── evaluator.py

│   ├── langfuse\_scores.py

│   ├── mock\_langfuse\_test.py

│   ├── run\_mock\_tests.py

│   ├── run\_tests.py

│   ├── test\_cases.json

│   └── README.md

│

├── tests/

│   ├── mock\_responses.py

│   └── test\_langfuse.py

│

├── .env.example

├── .gitignore

├── requirements.txt

└── README.md

```



\## Installation and Setup



\### 1. Clone the Repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



\### 2. Navigate to the Project



```bash

cd AI\_Customer\_Support\_Chatbot

```



\### 3. Create a Virtual Environment



```bash

python -m venv venv

```



\### 4. Activate the Environment



For Windows:



```powershell

venv\\Scripts\\activate

```



\### 5. Install Dependencies



```bash

pip install -r requirements.txt

```



\### 6. Configure Environment Variables



Create a `.env` file using `.env.example` as a reference.



Add your own Gemini and Langfuse credentials locally.



Never upload API keys or secret credentials to GitHub.



\## Run the Application



```bash

streamlit run app/ui.py

```



\## Testing and Evaluation



Run mock evaluation:



```bash

python -m evaluation.run\_mock\_tests

```



Run the evaluation workflow:



```bash

python -m evaluation.run\_tests

```



\## Testing Focus



The project includes

