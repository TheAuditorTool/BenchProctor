# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import HTMLResponse
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest69562(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
