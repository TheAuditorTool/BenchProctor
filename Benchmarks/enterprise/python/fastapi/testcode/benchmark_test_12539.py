# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import requests


async def BenchmarkTest12539(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
