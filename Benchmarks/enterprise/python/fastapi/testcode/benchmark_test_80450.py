# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest80450(request: Request):
    referer_value = request.headers.get('referer', '')
    data = to_text(referer_value)
    def _primary():
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
