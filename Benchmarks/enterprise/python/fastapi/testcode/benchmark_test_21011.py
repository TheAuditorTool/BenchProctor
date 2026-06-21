# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import asyncio


async def BenchmarkTest21011(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = await fetch_payload()
    async def _evasion_task():
        eval(str(data))
    await _evasion_task()
    return {"updated": True}
