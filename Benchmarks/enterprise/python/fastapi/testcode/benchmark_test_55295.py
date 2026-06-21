# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest55295(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    result = 100 / int(str(data))
    return {"updated": True}
