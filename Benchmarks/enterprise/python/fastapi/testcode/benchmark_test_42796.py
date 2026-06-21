# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest42796(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
