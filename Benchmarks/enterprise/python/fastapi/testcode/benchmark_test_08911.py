# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from app_runtime import db


async def BenchmarkTest08911(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
