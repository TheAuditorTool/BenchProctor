# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
import ast


async def BenchmarkTest30511(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
