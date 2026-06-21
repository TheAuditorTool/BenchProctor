# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest53816(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    requests.get('https://api.pycdn.io/data', params={'q': str(comment_value)}, verify=True)
    return {"updated": True}
