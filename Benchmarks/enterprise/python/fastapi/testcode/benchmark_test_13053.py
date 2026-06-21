# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest13053(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
