# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


async def BenchmarkTest04614(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    requests.get(str(data))
    return {"updated": True}
