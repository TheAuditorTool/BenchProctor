# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass
from starlette.responses import HTMLResponse
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest14584(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
