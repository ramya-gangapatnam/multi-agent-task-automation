from autogen_agentchat.agents import AssistantAgent

from app.model_client import get_model_client


def create_planner_agent() -> AssistantAgent:
    """
    Create the Planner Agent.

    This agent breaks a high-level task into clear, ordered steps
    that other agents can execute.
    """
    return AssistantAgent(
        name="planner_agent",
        model_client=get_model_client(),
        system_message=(
            "You are a task planning agent.\n"
            "Your job is to break a user's request into a short, clear, ordered plan.\n"
            "Return 3 to 6 practical steps.\n"
            "Do not solve the task.\n"
            "Do not add extra explanation.\n"
            "Keep steps concise and actionable."
        ),
    )


def create_planner_agent() -> AssistantAgent:
    """
    Create the Planner Agent.

    This agent breaks a high-level task into clear, ordered steps
    that other agents can execute.
    """
    return AssistantAgent(
        name="planner_agent",
        model_client=get_model_client(),
        system_message=(
            "You are a task planning agent.\n"
            "Your job is to break a user's request into a short, clear, ordered plan.\n"
            "Return 3 to 6 practical steps.\n"
            "Do not solve the task.\n"
            "Do not add extra explanation.\n"
            "Keep steps concise and actionable."
        ),
    )


def create_research_agent() -> AssistantAgent:
    """
    Create the Research Agent.

    This agent takes a task and a plan, then produces a focused research summary
    that will later be used by downstream agents.
    """
    return AssistantAgent(
        name="research_agent",
        model_client=get_model_client(),
        system_message=(
            "You are a research agent.\n"
            "Your job is to gather and organize useful information based on the user's task and the provided plan.\n"
            "Do not invent facts.\n"
            "If information is uncertain, clearly say so.\n"
            "Return a concise but useful research summary that another agent can analyze."
        ),
    )

def create_analyst_agent() -> AssistantAgent:
    """
    Create the Analyst Agent.

    This agent interprets research findings, identifies key takeaways,
    and produces a more decision-ready summary.
    """
    return AssistantAgent(
        name="analyst_agent",
        model_client=get_model_client(),
        system_message=(
            "You are an analysis agent.\n"
            "Your job is to interpret research findings and produce a clear, structured analysis.\n"
            "Highlight key insights, risks, tradeoffs, and useful conclusions.\n"
            "Do not invent facts beyond the provided material.\n"
            "If something is uncertain, say so clearly.\n"
            "Write in a concise, professional tone."
        ),
    )