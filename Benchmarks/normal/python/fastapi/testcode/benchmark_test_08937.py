# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest08937(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = f'{graphql_var}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
