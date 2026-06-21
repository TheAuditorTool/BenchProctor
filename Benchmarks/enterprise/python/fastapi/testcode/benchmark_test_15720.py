# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


async def BenchmarkTest15720(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
