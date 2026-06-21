# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest43507(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    exec(str(data))
    return {"updated": True}
