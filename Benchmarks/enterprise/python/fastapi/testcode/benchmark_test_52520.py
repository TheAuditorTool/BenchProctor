# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


async def BenchmarkTest52520(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    requests.post('http://api.prod.internal/data', data=str(env_value))
    return {"updated": True}
