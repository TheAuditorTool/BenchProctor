# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest13692(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
