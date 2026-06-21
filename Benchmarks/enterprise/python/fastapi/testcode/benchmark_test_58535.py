# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import json
from app_runtime import auth_check


async def BenchmarkTest58535(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
