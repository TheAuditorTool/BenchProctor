# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest61975(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    json.loads(data)
    return {"updated": True}
