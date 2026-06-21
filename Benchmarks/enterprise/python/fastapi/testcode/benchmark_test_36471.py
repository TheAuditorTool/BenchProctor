# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest36471(request: Request):
    origin_value = request.headers.get('origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
