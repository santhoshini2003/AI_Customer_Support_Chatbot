# AI Customer Support Chatbot

An AI-powered customer support chatbot built with **Python** and **Google Gemini API**. The project generates responses to customer queries, validates AI-generated responses, and includes automated testing and evaluation workflows using **Langfuse**.

## Project Overview

The AI Customer Support Chatbot is designed to provide relevant and reliable responses to customer-support queries using a Large Language Model (LLM).

The project focuses on:

- AI-based customer query handling
- Prompt engineering
- Response validation
- Safety-focused response checks
- Automated testing
- Offline mock evaluation
- AI response evaluation and monitoring

## Key Features

- AI-powered customer support response generation
- Google Gemini API integration
- Prompt engineering for customer-support scenarios
- Response validation and safety checks
- Handling of inappropriate and out-of-scope requests
- Prompt injection resistance testing
- Unknown-answer and hallucination handling
- Automated test case execution
- Offline mock-based evaluation
- Langfuse integration for AI evaluation tracking
- Environment-variable based API key management

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Google Gemini API | AI response generation |
| Streamlit | Chatbot interface |
| Langfuse | LLM monitoring and evaluation |
| Python-dotenv | Environment variable management |

## Project Structure

```text
AI_Customer_Support_Chatbot/
│
├── app/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── config.py
│   ├── llm_client.py
│   ├── prompts.py
│   ├── ui.py
│   └── validators.py
│
├── data/
│
├── evaluation/
│   ├── evaluator.py
│   ├── langfuse_scores.py
│   ├── mock_langfuse_test.py
│   ├── mock_results.json
│   ├── results.json
│   ├── run_mock_tests.py
│   ├── run_tests.py
│   ├── test_cases.json
│   └── README.md
│
├── tests/
│   ├── mock_responses.py
│   └── test_langfuse.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/santhoshini2003/AI_Customer_Support_Chatbot.git
```

### 2. Navigate to the Project

```bash
cd AI_Customer_Support_Chatbot
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

For Windows:

```powershell
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root using `.env.example` as a reference.

Add your own API credentials locally.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Never upload real API keys, passwords, or other secret credentials to GitHub.

## Run the Application

Start the Streamlit application:

```bash
streamlit run app/ui.py
```

## Testing and Evaluation

### Run Offline Mock Evaluation

The project supports offline mock evaluation so that the evaluation workflow can be tested without depending on live LLM responses.

```bash
python -m evaluation.run_mock_tests
```

### Run the Evaluation Workflow

```bash
python -m evaluation.run_tests
```

## Evaluation Test Cases

The evaluation suite currently includes five test scenarios:

| Test Case | Focus |
|---|---|
| TC001 | Functional response |
| TC002 | Privacy handling |
| TC003 | Prompt injection |
| TC004 | Hallucination / unknown answer |
| TC005 | Out-of-scope request |

## Response Validation

Before AI responses are evaluated, basic validation checks are applied.

The validator checks for:

- Empty responses
- Potential API key leakage
- System prompt leakage
- Internal instruction leakage

## Evaluation Module

The `evaluation/` module contains the scripts and test data used to evaluate chatbot behavior.

It covers:

- Functional behavior
- Privacy protection
- Prompt injection resistance
- Hallucination and unknown-answer handling
- Out-of-scope request handling
- Mock-based evaluation
- Langfuse evaluation tracking

More details are available in [`evaluation/README.md`](evaluation/README.md).

## Security

- API keys are stored using environment variables.
- `.env` is excluded from Git version control.
- `venv` and Python cache files are excluded from Git.
- Real API credentials should never