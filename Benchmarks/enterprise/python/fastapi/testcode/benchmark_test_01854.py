# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import requests


async def BenchmarkTest01854(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
