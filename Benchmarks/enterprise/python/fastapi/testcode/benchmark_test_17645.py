# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest17645(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
