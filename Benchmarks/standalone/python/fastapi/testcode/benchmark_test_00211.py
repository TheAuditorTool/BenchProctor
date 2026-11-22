# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
import ldap
from starlette.responses import JSONResponse
import os
from pydantic import Field, ValidationError, create_model
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


@app.post("/BenchmarkTest00211")
async def BenchmarkTest00211(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    kind = 'json' if str(db_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(db_value).strip()
        case _:
            data = str(db_value)
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.#%\\-]+$")))(value=str(data))
    except ValidationError:
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    conn = ldap.initialize(os.environ.get('LDAP_URL', 'ldap://directory:1389'))
    conn.compare_s('uid=' + str(processed) + ',ou=people,dc=example,dc=com', 'employeeType', b'staff')
    return {"updated": True}
