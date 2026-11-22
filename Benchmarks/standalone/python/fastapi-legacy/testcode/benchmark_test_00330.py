# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from app_runtime import db
from fastapi.responses import JSONResponse


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00330")
async def BenchmarkTest00330(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = '%s' % str(file_value)
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return {"updated": True}
