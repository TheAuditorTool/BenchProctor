# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest69284(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
