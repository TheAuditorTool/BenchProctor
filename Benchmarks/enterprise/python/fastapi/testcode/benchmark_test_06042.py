# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


def normalise_input(value):
    return value.strip()

async def BenchmarkTest06042(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
