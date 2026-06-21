# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest16111(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
