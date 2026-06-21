# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest77116(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
