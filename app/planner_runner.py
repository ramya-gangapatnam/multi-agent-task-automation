import asyncio
import logging

from app.agents import create_planner_agent
from app.config import validate_config
from app.logging_config import setup_logging


setup_logging()
logger = logging.getLogger(__name__)
validate_config()


async def run_planner(task: str) -> str:
    """
    Run the planner agent for a single task and return its response text.
    """
    planner = create_planner_agent()

    result = await planner.run(task=task)

    # AutoGen agent result objects typically expose the final text through .messages
    # We keep this simple for now and return the most recent message content.
    if not result.messages:
        raise ValueError("Planner agent returned no messages.")

    final_message = result.messages[-1]
    content = getattr(final_message, "content", None)

    if not content:
        raise ValueError("Planner agent returned an empty response.")

    return content


if __name__ == "__main__":
    sample_task = "Research Tesla stock and summarize key risks for a beginner investor."
    output = asyncio.run(run_planner(sample_task))
    print("\nPlanner Output:\n")
    print(output)