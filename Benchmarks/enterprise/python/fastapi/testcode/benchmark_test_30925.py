# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json


async def BenchmarkTest30925(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    globals()['counter'] = int(data)
    return {"updated": True}
