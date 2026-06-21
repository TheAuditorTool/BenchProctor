# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
import json


async def BenchmarkTest44482(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
