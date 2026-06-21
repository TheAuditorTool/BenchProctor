# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest63724(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
