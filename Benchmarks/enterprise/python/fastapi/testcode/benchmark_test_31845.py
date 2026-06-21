# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest31845(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if not str(graphql_var).isdigit():
        raise ValueError('invalid input: ' + str(graphql_var))
    return {"updated": True}
