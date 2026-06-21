# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest27080(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
