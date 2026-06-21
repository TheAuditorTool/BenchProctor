# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


async def BenchmarkTest52168(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(comment_value)
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
