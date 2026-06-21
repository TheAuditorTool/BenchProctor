# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import asyncio


async def BenchmarkTest04613(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = await fetch_payload()
    processed = data[:64]
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return {"updated": True}
