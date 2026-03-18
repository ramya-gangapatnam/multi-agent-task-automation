import logging

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from app.config import validate_config
from app.logging_config import setup_logging
from app.orchestrator_runner import run_orchestration
from app.schemas import ErrorResponse, FinalResponse, TaskRequest


setup_logging()
logger = logging.getLogger(__name__)
validate_config()

app = FastAPI(
    title="Multi-Agent AI Task Automation System",
    version="1.0.0",
    description="FastAPI service for running a multi-agent workflow with planning, research, analysis, review, and final response generation.",
)


@app.get("/health")
def health_check() -> dict:
    """
    Simple health check endpoint.
    """
    return {"status": "ok"}


@app.post("/run-task", response_model=FinalResponse)
async def run_task(request: TaskRequest) -> FinalResponse:
    """
    Run the multi-agent workflow for a user-provided task.
    """
    try:
        full_task = request.task.strip()

        if request.context:
            full_task = f"{full_task}\n\nAdditional context:\n{request.context.strip()}"

        result = await run_orchestration(full_task)

        cleaned_plan_steps = [
            line.strip()
            for line in result["plan"].splitlines()
            if line.strip()
        ]

        return FinalResponse(
            task=result["task"],
            plan_steps=cleaned_plan_steps,
            research_output=result["research"],
            analysis_output=result["analysis"],
            review_output=result["review"],
            final_answer=result["final_answer"],
        )

    except ValueError as exc:
        logger.exception("Task validation failed")
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception:
        logger.exception("Task execution failed")
        raise HTTPException(status_code=500, detail="Internal server error during task execution.")


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """
    Catch unexpected errors and return a consistent JSON response.
    """
    logger.exception("Unhandled application error")
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            message="An unexpected internal server error occurred."
        ).model_dump(),
    )