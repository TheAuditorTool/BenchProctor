# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import json
from app_runtime import db


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00043")
async def BenchmarkTest00043(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    if label is None:
        return JSONResponse({'error': 'unknown plan'}, status_code=404)
    value = label.upper()
    return JSONResponse({'plan': value}, status_code=200)
