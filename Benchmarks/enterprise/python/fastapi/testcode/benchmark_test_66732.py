# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest66732(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = forwarded_ip if forwarded_ip else 'default'
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
