# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest73804(request: Request):
    origin_value = request.headers.get('origin', '')
    _resp = requests.get(str(origin_value))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
