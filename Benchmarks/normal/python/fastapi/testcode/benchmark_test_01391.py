# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest01391(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
