# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata
from app_runtime import db


async def BenchmarkTest41859(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
