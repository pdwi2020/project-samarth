from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .analytics import AnalyticsEngine
from .config import load_config
from .data_manager import DataManager
from .question_parser import parse_question


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str
    tables: list
    citations: list
    debug: dict | None = None


app = FastAPI(title="Project Samarth Prototype", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

config = load_config()
data_manager = DataManager(config)
analytics = AnalyticsEngine(data_manager)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest):
    parsed = parse_question(payload.question)
    params = parsed.params

    try:
        if parsed.intent == "compare_rainfall_and_crops":
            for key in ("state_a", "state_b"):
                if not params.get(key):
                    raise HTTPException(status_code=422, detail="Could not detect both states in the question.")
            answer = analytics.compare_rainfall_and_crops(
                state_a=params["state_a"],
                state_b=params["state_b"],
                crop_filter=params.get("crop_filter"),
                last_n_years=params.get("years"),
                top_m=params.get("top_m", 3),
            )
        elif parsed.intent == "district_extremes":
            for key in ("state_a", "state_b", "crop"):
                if not params.get(key):
                    raise HTTPException(status_code=422, detail="Missing states or crop in the question.")
            answer = analytics.district_extremes(
                state_a=params["state_a"],
                state_b=params["state_b"],
                crop=params["crop"],
                year=params.get("year"),
            )
        elif parsed.intent == "production_trend_with_climate":
            for key in ("region", "crop"):
                if not params.get(key):
                    raise HTTPException(status_code=422, detail="Missing region or crop.")
            answer = analytics.production_trend_with_climate(
                region=params["region"],
                crop=params["crop"],
                years=params.get("years"),
            )
        elif parsed.intent == "policy_arguments":
            for key in ("region", "crop_a", "crop_b"):
                if not params.get(key):
                    raise HTTPException(status_code=422, detail="Need region and both crop types.")
            answer = analytics.policy_arguments(
                region=params["region"],
                crop_a=params["crop_a"],
                crop_b=params["crop_b"],
                years=params.get("years"),
            )
        else:
            return AskResponse(
                answer="Sorry, I could not recognise that question pattern yet.",
                tables=[],
                citations=[],
                debug={"intent": parsed.intent},
            )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return AskResponse(**answer.to_dict())


@app.post("/refresh")
def refresh():
    analytics.refresh()
    return {"status": "reloaded"}
