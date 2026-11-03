import sys
import os
import json
from datetime import datetime

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from app.validators import validate_response
from evaluation.evaluator import evaluate_response
from tests.mock_responses import MOCK_RESPONSES


def load_test_cases():

    with open(
        "evaluation/test_cases.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def run_mock_tests():

    test_results = []

    test_cases = load_test_cases()

    total_tests = len(test_cases)
    passed_tests = 0
    failed_tests = 0
    total_score = 0

    print("=" * 70)
    print("OFFLINE AI MODEL EVALUATION")
    print("=" * 70)

    for test_case in test_cases:

        test_id = test_case["test_id"]
        category = test_case["category"]

        response = MOCK_RESPONSES[test_id]

        print("\n" + "-" * 70)

        print(f"Test ID  : {test_id}")
        print(f"Category : {category}")

        print("\nMock AI Response:")
        print(response)

        # Basic validation
        validation = validate_response(response)

        print("\nBasic Validation:")

        print(
            f"Status : "
            f"{'PASS' if validation['valid'] else 'FAIL'}"
        )

        print(
            f"Reason : {validation['reason']}"
        )

        # Stop evaluation if validation fails
        if not validation["valid"]:

            print(
                "\nAI Evaluation: SKIPPED"
            )

            failed_tests += 1

            continue

        # Evaluate response
        evaluation = evaluate_response(
            test_case,
            response
        )

        score = evaluation["score"]
        passed = evaluation["passed"]

        total_score += score

        print("\nAI Evaluation:")

        for check in evaluation["checks"]:

            print(
                f"  - {check}"
            )

        print(
            f"\nScore  : {score}/10"
        )

        print(
            f"Result : "
            f"{'PASS' if passed else 'FAIL'}"
        )

        if passed:

            passed_tests += 1

        else:

            failed_tests += 1

        test_results.append({
            "test_id": test_id,
            "category": category,
            "validation": validation,
            "score": score,
            "result": "PASS" if passed else "FAIL"
        })

    # Final calculations

    average_score = (
        total_score / total_tests
    )

    pass_rate = (
        passed_tests / total_tests
    ) * 100

    print("\n" + "=" * 70)
    print("OFFLINE EVALUATION SUMMARY")
    print("=" * 70)

    print(
        f"Total Tests      : {total_tests}"
    )

    print(
        f"Passed Tests     : {passed_tests}"
    )

    print(
        f"Failed Tests     : {failed_tests}"
    )

    print(
        f"Pass Rate        : {pass_rate:.2f}%"
    )

    print(
        f"Average AI Score : "
        f"{average_score:.2f}/10"
    )

    results = {
        "project": "AI Customer Support Chatbot",
        "evaluation_type": "offline_mock",
        "evaluation_timestamp": datetime.now().isoformat(),
        "summary": {
            "total_tests": total_tests,
            "passed_tests": passed_tests,
            "failed_tests": failed_tests,
            "pass_rate": round(pass_rate, 2),
            "average_score": round(average_score, 2)
        },
        "test_results": test_results
    }

    with open(
        "evaluation/mock_results.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\nMock results saved to:")
    print("evaluation/mock_results.json")

    print("=" * 70)


if __name__ == "__main__":
    run_mock_tests()