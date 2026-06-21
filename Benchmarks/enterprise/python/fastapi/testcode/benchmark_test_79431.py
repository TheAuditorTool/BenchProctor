# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from app_runtime import db


async def BenchmarkTest79431(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    processed = html.escape(comment_value)
    return HTMLResponse('<div>' + str(processed) + '</div>')
