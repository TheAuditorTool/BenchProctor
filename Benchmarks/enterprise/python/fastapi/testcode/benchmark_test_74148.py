# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest74148(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
