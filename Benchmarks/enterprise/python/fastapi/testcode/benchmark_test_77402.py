# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import re
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest77402(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    requests.get(str(data))
    return {"updated": True}
