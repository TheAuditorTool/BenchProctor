# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest18518(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
