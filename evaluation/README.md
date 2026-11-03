# AI Customer Support Chatbot - Evaluation Module

## Purpose

This module evaluates the AI Customer Support Chatbot for
quality, safety, reliability, and domain compliance.

## Evaluation Categories

The evaluation framework currently covers:

1. Functional behavior
2. Privacy protection
3. Prompt injection resistance
4. Hallucination prevention
5. Out-of-scope request handling

## Test Dataset

The evaluation test cases are stored in:

`test_cases.json`

Currently the test suite contains:

- TC001 - Functional
- TC002 - Privacy
- TC003 - Prompt Injection
- TC004 - Hallucination
- TC005 - Out of Scope

## Response Validation

Before AI responses are scored, basic validation checks are applied.

The validator checks for:

- Empty responses
- API key leakage
- System prompt leakage
- Internal instruction leakage

## Offline Evaluation

The project supports offline mock evaluation so that the
evaluation framework can be tested independently of the LLM API.

Run:

```bash
python -m evaluation.run_mock_tests