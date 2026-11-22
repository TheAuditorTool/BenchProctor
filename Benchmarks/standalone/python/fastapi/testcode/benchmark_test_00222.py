# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import random
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


@app.post("/BenchmarkTest00222")
async def BenchmarkTest00222(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(graphql_var).strip()
        case _:
            data = str(graphql_var)
    token = random.randbytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JSONResponse({'token': str(token)}, status_code=200)
