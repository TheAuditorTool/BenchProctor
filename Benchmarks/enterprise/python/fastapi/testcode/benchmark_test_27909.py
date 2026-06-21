# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest27909(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        result = int(str(graphql_var))
    except Exception:
        pass
    return {"updated": True}
