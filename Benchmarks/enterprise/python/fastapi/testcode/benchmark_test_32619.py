# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest32619(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
