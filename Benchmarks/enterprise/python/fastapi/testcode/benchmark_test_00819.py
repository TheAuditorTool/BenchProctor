# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import auth_check


async def BenchmarkTest00819(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    auth_check('user', data)
    return {"updated": True}
