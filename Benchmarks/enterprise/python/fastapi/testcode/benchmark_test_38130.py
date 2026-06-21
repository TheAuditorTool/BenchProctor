# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest38130(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    eval(str(data))
    return {"updated": True}
