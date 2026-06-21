# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


async def BenchmarkTest50537(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(graphql_var)}, verify=True)
    return {"updated": True}
