# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from types import SimpleNamespace


async def BenchmarkTest49227(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ns = SimpleNamespace(payload=dotenv_value)
    data = getattr(ns, 'payload')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
