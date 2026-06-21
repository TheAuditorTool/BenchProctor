# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


def to_text(value):
    return str(value).strip()

async def BenchmarkTest05162(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
