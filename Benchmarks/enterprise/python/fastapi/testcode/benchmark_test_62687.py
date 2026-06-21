# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest62687(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    globals()['counter'] = int(data)
    return {"updated": True}
