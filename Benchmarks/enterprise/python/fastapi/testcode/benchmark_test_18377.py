# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from app_runtime import db


async def BenchmarkTest18377(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
