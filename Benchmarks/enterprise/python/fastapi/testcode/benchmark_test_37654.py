# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import time


async def BenchmarkTest37654(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
