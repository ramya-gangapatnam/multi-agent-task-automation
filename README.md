# Multi-Agent AI Task Automation System

A multi-agent system that breaks down complex tasks into structured steps and executes them using specialized AI agents.

## Overview

This project demonstrates how multiple AI agents can collaborate to solve a task through planning, research, analysis, review, and final response generation.

Each agent is responsible for a specific role, enabling more structured and reliable outputs compared to single-prompt systems.

---

## Tech Stack

- Python
- AutoGen (AgentChat)
- OpenAI API
- yfinance (external API integration)

---

## How It Works

1. Planner Agent creates a step-by-step plan  
2. Research Agent gathers information (uses external APIs when needed)  
3. Analyst Agent interprets the research  
4. Reviewer Agent checks for clarity, gaps, and issues  
5. Final Response Agent produces a clean user-facing answer  

---

## Project Structure
# Multi-Agent AI Task Automation System

A multi-agent system that breaks down complex tasks into structured steps and executes them using specialized AI agents.

## Overview

This project demonstrates how multiple AI agents can collaborate to solve a task through planning, research, analysis, review, and final response generation.

Each agent is responsible for a specific role, enabling more structured and reliable outputs compared to single-prompt systems.

---

## Tech Stack

- Python
- AutoGen (AgentChat)
- OpenAI API
- yfinance (external API integration)

---

## How It Works

1. Planner Agent creates a step-by-step plan  
2. Research Agent gathers information (uses external APIs when needed)  
3. Analyst Agent interprets the research  
4. Reviewer Agent checks for clarity, gaps, and issues  
5. Final Response Agent produces a clean user-facing answer  

---

## Project Structure
app/
├── agents.py
├── config.py
├── logging_config.py
├── model_client.py
├── orchestrator_runner.py
├── planner_runner.py
├── schemas.py
├── tools/
│ └── stock_tool.py


---

## Key Features

- Multi-agent orchestration with role-based agents
- Task decomposition using a planner agent
- External API integration (stock data via yfinance)
- Tool-calling within agent workflows
- Structured logging across agent stages
- Output normalization to ensure clean responses
- Reviewer agent to improve output quality

---

## Example Flow

Input:
Analyze Tesla stock and summarize key risks for a beginner investor


System Flow:
- Planner → creates steps  
- Research → fetches real data  
- Analyst → generates insights  
- Reviewer → validates output  
- Final agent → produces answer  

Output:
- Clean, structured, beginner-friendly response

---

## How to Run

1. Create virtual environment
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Add environment variables
Create .env:
OPENAI_API_KEY=your_key_here
MODEL_NAME=gpt-4.1-mini

4. Run the system
python -m app.orchestrator_runner

Possible Improvements:
Add FastAPI endpoints for real-time usage
Add memory across tasks
Add evaluation metrics for agent performance
Add caching for tool calls
Support multiple tools beyond stock data

What This Project Demonstrates:
Multi-agent system design
Agent orchestration and role separation
Tool-augmented AI workflows
Production-minded logging and output control
