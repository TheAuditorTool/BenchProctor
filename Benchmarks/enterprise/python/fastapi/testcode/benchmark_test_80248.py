# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from dataclasses import dataclass
from starlette.responses import JSONResponse
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest80248(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
