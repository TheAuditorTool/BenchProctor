# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import ldap3
from starlette.responses import JSONResponse
import os
from pydantic import Field, ValidationError, create_model


app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00093")
async def BenchmarkTest00093(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    try:
        create_model('_InputModel', value=(str, Field(regex="^[a-zA-Z0-9 _.#%\\-]+$")))(value=str(data))
    except ValidationError:
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    conn = ldap3.Connection(ldap3.Server(os.environ.get('LDAP_URL', 'ldap://directory:1389')), auto_bind=True)
    conn.search('dc=example,dc=com', '(uid=' + str(processed) + ')', attributes=['cn'])
    return {"updated": True}
