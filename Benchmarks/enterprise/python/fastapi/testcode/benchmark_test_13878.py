# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import ast
from app_runtime import db


async def BenchmarkTest13878(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    async def _evasion_task():
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    await _evasion_task()
    return {"updated": True}
