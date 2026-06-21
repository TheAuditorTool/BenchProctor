# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


async def BenchmarkTest25155(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    requests.get(str(data))
    return {"updated": True}
