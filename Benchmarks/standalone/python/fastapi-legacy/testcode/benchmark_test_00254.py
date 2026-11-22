# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00254")
async def BenchmarkTest00254(request: Request):
    user_id = request.query_params.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(user_id).strip()
        case _:
            data = str(user_id)
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    value = label.upper()
    return JSONResponse({'plan': value}, status_code=200)
