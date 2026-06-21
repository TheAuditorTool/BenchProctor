# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest13184(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if not str(graphql_var).isdigit():
        raise Exception('error: ' + str(graphql_var))
    return {"updated": True}
