# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


async def BenchmarkTest75721(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    parts = []
    for token in str(dotenv_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
