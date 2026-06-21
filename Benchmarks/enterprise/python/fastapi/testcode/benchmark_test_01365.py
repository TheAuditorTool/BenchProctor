# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest01365(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    int(str(data))
    return {"updated": True}
