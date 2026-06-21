# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


async def BenchmarkTest24185(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
