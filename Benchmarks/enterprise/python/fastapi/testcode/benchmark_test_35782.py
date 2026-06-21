# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest35782(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
