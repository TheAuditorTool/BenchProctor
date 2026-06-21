# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
from app_runtime import db


async def BenchmarkTest69982(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
