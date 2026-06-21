# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import defusedxml.ElementTree


async def BenchmarkTest03290(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
