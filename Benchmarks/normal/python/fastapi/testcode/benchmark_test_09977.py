# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from starlette.responses import HTMLResponse
import unicodedata
from app_runtime import db


async def BenchmarkTest09977(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
