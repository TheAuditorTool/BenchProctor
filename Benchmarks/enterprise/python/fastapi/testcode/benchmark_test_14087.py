# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import time
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest14087(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = default_blank(comment_value)
    if time.time() > 1000000000:
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
