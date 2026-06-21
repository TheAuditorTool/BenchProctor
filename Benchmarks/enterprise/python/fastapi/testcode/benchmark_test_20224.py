# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def relay_value(value):
    return value

async def BenchmarkTest20224(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
