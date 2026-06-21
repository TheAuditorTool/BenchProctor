# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


async def BenchmarkTest15857(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    pending = list(str(dotenv_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
