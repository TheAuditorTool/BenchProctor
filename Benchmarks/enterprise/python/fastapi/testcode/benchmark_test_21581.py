# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest21581(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    int(str(data))
    return {"updated": True}
