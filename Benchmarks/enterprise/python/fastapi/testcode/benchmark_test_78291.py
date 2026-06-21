# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json
import ast


_shared_counter_lock = threading.Lock()

async def BenchmarkTest78291(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
