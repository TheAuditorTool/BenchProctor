# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest40442(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
