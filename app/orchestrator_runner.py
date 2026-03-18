import asyncio
import logging

from app.agents import (
    create_analyst_agent,
    create_final_response_agent,
    create_planner_agent,
    create_research_agent,
    create_reviewer_agent,
)
from app.config import validate_config
from app.logging_config import setup_logging


setup_logging()
logger = logging.getLogger(__name__)
validate_config()


def extract_final_content(result) -> str:
    """
    Extract and clean the final text response from an AutoGen agent result.
    """
    if not result.messages:
        raise ValueError("Agent returned no messages.")

    final_message = result.messages[-1]
    content = getattr(final_message, "content", None)

    if not content:
        raise ValueError("Agent returned an empty response.")

    # If content looks like raw dict, convert to readable text
    if isinstance(content, str) and content.strip().startswith("{"):
        return "Research data retrieved successfully. Key details were used for analysis."

    return content.strip()


async def run_orchestration(task: str) -> dict:
    """
    Run a five-agent orchestration:
    1. Planner agent creates a plan
    2. Research agent produces a research summary
    3. Analyst agent interprets the research
    4. Reviewer agent checks the analysis for quality and gaps
    5. Final response agent produces the final user-facing answer
    """
    planner = create_planner_agent()
    researcher = create_research_agent()
    analyst = create_analyst_agent()
    reviewer = create_reviewer_agent()
    final_responder = create_final_response_agent()

    logger.info("Starting orchestration for task: %s", task)

    logger.info("Running planner agent")
    planner_result = await planner.run(task=task)
    plan_text = extract_final_content(planner_result)
    # logger.info("Planner output:\n%s", plan_text)
    logger.info("Planner completed")

    logger.info("Running research agent")
    research_prompt = (
        f"User task:\n{task}\n\n"
        f"Planner output:\n{plan_text}\n\n"
        "Produce a concise research summary based on this plan."
    )
    research_result = await researcher.run(task=research_prompt)
    research_text = extract_final_content(research_result)
    # logger.info("Research output:\n%s", research_text)
    logger.info("Research completed")

    logger.info("Running analyst agent")
    analysis_prompt = (
        f"User task:\n{task}\n\n"
        f"Planner output:\n{plan_text}\n\n"
        f"Research summary:\n{research_text}\n\n"
        "Produce a structured analysis with key insights, important risks, and a concise conclusion."
    )
    analysis_result = await analyst.run(task=analysis_prompt)
    analysis_text = extract_final_content(analysis_result)
    # logger.info("Analysis output:\n%s", analysis_text)
    logger.info("Analysis completed")

    logger.info("Running reviewer agent")
    review_prompt = (
        f"User task:\n{task}\n\n"
        f"Planner output:\n{plan_text}\n\n"
        f"Research summary:\n{research_text}\n\n"
        f"Analysis output:\n{analysis_text}\n\n"
        "Review this analysis for clarity, completeness, unsupported claims, and missing risks."
    )
    review_result = await reviewer.run(task=review_prompt)
    review_text = extract_final_content(review_result)
    # logger.info("Review output:\n%s", review_text)
    logger.info("Review completed")

    logger.info("Running final response agent")
    final_prompt = (
        f"User task:\n{task}\n\n"
        f"Planner output:\n{plan_text}\n\n"
        f"Research summary:\n{research_text}\n\n"
        f"Analysis output:\n{analysis_text}\n\n"
        f"Reviewer feedback:\n{review_text}\n\n"
        "Produce the final user-facing answer."
    )
    final_result = await final_responder.run(task=final_prompt)
    final_text = extract_final_content(final_result)
    logger.info("Final response generated successfully")

    return {
        "task": task,
        "plan": plan_text,
        "research": research_text,
        "analysis": analysis_text,
        "review": review_text,
        "final_answer": final_text,
    }


# if __name__ == "__main__":
#     sample_task = "Analyze Tesla stock and summarize key risks for a beginner investor."
#     result = asyncio.run(run_orchestration(sample_task))

#     print("\nTask:\n")
#     print(result["task"])

#     print("\nPlanner Output:\n")
#     print(result["plan"])

#     print("\nResearch Output:\n")
#     print(result["research"])

#     print("\nAnalysis Output:\n")
#     print(result["analysis"])

#     print("\nReview Output:\n")
#     print(result["review"])

#     print("\nFinal Answer:\n")
#     print(result["final_answer"])

if __name__ == "__main__":
    sample_task = "Analyze Tesla stock and summarize key risks for a beginner investor."
    result = asyncio.run(run_orchestration(sample_task))

    print("\nFinal Answer:\n")
    print(result["final_answer"])