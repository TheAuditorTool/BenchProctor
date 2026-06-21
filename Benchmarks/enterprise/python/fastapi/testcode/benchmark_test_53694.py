# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json


_shared_counter_lock = threading.Lock()

async def BenchmarkTest53694(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = graphql_var
            data = parsed
        case _:
            data = graphql_var
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
