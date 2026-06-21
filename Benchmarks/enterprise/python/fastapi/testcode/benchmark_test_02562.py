# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


async def BenchmarkTest02562(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = (lambda v: v.strip())(dotenv_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
