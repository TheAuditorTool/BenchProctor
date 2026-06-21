# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def to_text(value):
    return str(value).strip()

async def BenchmarkTest13208(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
