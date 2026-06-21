# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest49372(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    requests.post('http://api.prod.internal/data', data=str(comment_value))
    return {"updated": True}
