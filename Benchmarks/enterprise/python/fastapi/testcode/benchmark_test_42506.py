# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest42506(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = []
    for token in str(graphql_var).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
