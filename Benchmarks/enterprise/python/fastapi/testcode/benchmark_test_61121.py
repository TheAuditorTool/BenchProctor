# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from app_runtime import auth_check


async def BenchmarkTest61121(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(graphql_var), store_cred)
    return {"updated": True}
