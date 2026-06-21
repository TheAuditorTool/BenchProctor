# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest75095(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
