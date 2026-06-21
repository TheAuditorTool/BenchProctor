# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest56287(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = RequestPayload(db_value).value
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
