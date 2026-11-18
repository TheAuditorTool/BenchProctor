# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import json


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00243")
async def BenchmarkTest00243(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(graphql_var).strip()
        case _:
            data = str(graphql_var)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
