# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def ensure_str(value):
    return str(value)

async def BenchmarkTest60957(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
