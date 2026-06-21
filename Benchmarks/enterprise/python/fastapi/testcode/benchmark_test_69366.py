# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import requests


async def BenchmarkTest69366(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(graphql_var)}, verify=False)
    return {"updated": True}
