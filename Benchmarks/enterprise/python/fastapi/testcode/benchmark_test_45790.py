# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import time
from app_runtime import db


async def BenchmarkTest45790(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    if time.time() > 1000000000:
        return RedirectResponse(url=str(data))
    return {"updated": True}
