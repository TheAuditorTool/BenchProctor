# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest59026(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
