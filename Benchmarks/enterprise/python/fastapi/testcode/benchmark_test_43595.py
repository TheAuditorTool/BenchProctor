# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest43595(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    int(str(data))
    return {"updated": True}
