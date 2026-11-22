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


@app.post("/BenchmarkTest00301")
async def BenchmarkTest00301(request: Request):
    upload_name = getattr((await request.form()).get('upload'), 'filename', '')
    data = ' '.join(str(upload_name).split())
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    if label is None:
        return JSONResponse({'error': 'unknown plan'}, status_code=404)
    value = label.upper()
    return JSONResponse({'plan': value}, status_code=200)
