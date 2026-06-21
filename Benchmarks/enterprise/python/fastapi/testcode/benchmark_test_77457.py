# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from app_runtime import auth_check


async def BenchmarkTest77457(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    auth_check('user', data)
    return {"updated": True}
