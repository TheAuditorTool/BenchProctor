# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import json


async def BenchmarkTest67431(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
