# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def normalise_input(value):
    return value.strip()

async def BenchmarkTest71016(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
