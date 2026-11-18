# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import re
from starlette.responses import JSONResponse
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


@app.post("/BenchmarkTest00616")
async def BenchmarkTest00616(request: Request):
    user_id = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    db.execute("SELECT * FROM users WHERE id = '" + str(processed) + "'")
    return {"updated": True}
