# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from starlette.responses import HTMLResponse
import json


async def BenchmarkTest27816(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    return HTMLResponse('<script src="' + str(data) + '"></script>')
