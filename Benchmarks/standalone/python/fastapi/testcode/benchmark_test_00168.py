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


@app.post("/BenchmarkTest00168")
async def BenchmarkTest00168(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    if label is None:
        return JSONResponse({'error': 'unknown plan'}, status_code=404)
    value = label.upper()
    return JSONResponse({'plan': value}, status_code=200)
