# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import requests


async def BenchmarkTest63749(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
