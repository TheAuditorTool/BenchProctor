# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest28142(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
