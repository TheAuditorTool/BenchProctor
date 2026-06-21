# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest08392(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
