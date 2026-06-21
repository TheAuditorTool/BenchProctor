# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


async def BenchmarkTest68942(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
