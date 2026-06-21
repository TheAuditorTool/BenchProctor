# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest43836(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
