# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from app_runtime import db


async def BenchmarkTest14558(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    _resp = requests.get(str(env_value))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
