# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import json
import asyncio


_shared_counter_lock = threading.Lock()

async def BenchmarkTest11552(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = await fetch_payload()
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
