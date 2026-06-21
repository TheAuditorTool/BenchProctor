# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest54222(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = graphql_var
            data = parsed
        case _:
            data = graphql_var
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
