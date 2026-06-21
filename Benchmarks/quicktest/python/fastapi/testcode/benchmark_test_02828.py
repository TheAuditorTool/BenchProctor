# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest02828(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
