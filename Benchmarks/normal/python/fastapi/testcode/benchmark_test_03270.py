# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest03270(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    request.session['user'] = str(data)
    return {"updated": True}
