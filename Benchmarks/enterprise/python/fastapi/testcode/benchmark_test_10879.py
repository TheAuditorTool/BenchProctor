# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest10879(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    eval(str(data))
    return {"updated": True}
