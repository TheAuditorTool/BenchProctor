# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest80809(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    ns = SimpleNamespace(payload=profile_value)
    data = getattr(ns, 'payload')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
