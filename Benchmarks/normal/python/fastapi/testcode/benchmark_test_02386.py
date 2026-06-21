# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import socket


async def BenchmarkTest02386(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
