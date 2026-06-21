# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest55550(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = to_text(dotenv_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
