# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def normalise_input(value):
    return value.strip()

async def BenchmarkTest48990(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
