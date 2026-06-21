# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import socket


async def BenchmarkTest04619(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = graphql_var
            data = parsed
        case _:
            data = graphql_var
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
