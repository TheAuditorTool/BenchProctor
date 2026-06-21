# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest42721(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
