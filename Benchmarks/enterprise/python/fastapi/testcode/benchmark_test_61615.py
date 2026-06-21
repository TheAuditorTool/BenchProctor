# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest61615(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    eval(str(graphql_var))
    return {"updated": True}
