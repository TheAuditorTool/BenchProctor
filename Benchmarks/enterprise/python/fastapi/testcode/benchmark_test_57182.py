# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest57182(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
