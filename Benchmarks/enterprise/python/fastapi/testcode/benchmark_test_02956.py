# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest02956(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    request.session['data'] = str(data)
    return {"updated": True}
