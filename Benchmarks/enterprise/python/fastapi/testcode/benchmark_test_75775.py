# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest75775(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request.session['data'] = str(graphql_var)
    return {"updated": True}
