# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import json
from starlette.responses import JSONResponse
import importlib


def _revive_typed(fields):
    type_name = fields.pop('__type__', None)
    if type_name is None:
        return fields
    module_name, _, class_name = type_name.rpartition('.')
    return getattr(importlib.import_module(module_name), class_name)(**fields)

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00360")
async def BenchmarkTest00360(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    pending = list(str(forwarded_ip).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(data))
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
