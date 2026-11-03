from langfuse import get_client


langfuse = get_client()


def record_evaluation_score(
    trace_id: str,
    score: float,
    passed: bool,
    category: str
):
    """
    Record AI evaluation result in Langfuse.
    """

    langfuse.create_score(
        trace_id=trace_id,
        name="ai_quality_score",
        value=score,
        comment=(
            f"Category: {category} | "
            f"Result: {'PASS' if passed else 'FAIL'}"
        )
    )

    langfuse.create_score(
        trace_id=trace_id,
        name="evaluation_pass",
        value=1 if passed else 0,
        comment=f"Evaluation result for {category}"
    )

    langfuse.flush()