import json

from dotenv import load_dotenv
load_dotenv()

from langfuse import get_client

from evaluation.langfuse_scores import record_evaluation_score


langfuse = get_client()


def load_mock_results():

    with open(
        "evaluation/mock_results.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def main():

    print("=" * 70)
    print("MOCK EVALUATION -> LANGFUSE")
    print("=" * 70)

    results = load_mock_results()

    test_results = results["test_results"]

    print(
        f"\nLoading {len(test_results)} evaluation results..."
    )

    for test in test_results:

        test_id = test["test_id"]
        category = test["category"]
        score = test["score"]
        passed = test["result"] == "PASS"

        with langfuse.start_as_current_observation(
            name=f"mock_evaluation_{test_id}",
            as_type="generation",
            input={
                "test_id": test_id,
                "category": category
            },
            model="mock-model",
        ) as generation:

            generation.update(
                output={
                    "score": score,
                    "result": test["result"]
                },
                metadata={
                    "test_type": "offline_mock",
                    "test_id": test_id,
                    "category": category,
                },
            )

            trace_id = generation.trace_id

            record_evaluation_score(
                trace_id=trace_id,
                score=score,
                passed=passed,
                category=category,
            )

            print("\n" + "-" * 60)
            print(f"Test ID  : {test_id}")
            print(f"Category : {category}")
            print(f"Score    : {score}/10")
            print(
                f"Result   : "
                f"{'PASS' if passed else 'FAIL'}"
            )
            print(f"Trace ID : {trace_id}")

    langfuse.flush()

    print("\n" + "=" * 70)
    print("LANGFUSE MOCK EVALUATION COMPLETED")
    print("=" * 70)

    print(
        f"Total traces sent : {len(test_results)}"
    )

    print("Check the Langfuse dashboard.")
    print("=" * 70)


if __name__ == "__main__":
    main()