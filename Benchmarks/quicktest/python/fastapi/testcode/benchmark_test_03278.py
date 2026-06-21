# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest03278(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
