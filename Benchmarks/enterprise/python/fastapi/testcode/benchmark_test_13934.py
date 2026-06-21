# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from app_runtime import db


async def BenchmarkTest13934(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
