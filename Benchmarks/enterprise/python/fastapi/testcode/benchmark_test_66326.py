# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import base64
from app_runtime import db


async def BenchmarkTest66326(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
