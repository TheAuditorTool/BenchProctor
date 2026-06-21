# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest17875(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    int(str(graphql_var))
    return {"updated": True}
