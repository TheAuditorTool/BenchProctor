# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import socket


async def BenchmarkTest69625(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    s = socket.create_connection((str(graphql_var), 80))
    s.close()
    return {"updated": True}
