# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import asyncio
import pickle


async def BenchmarkTest04211(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = await fetch_payload()
    eval(compile("pickle.loads(data.encode('latin-1'))", '<sink>', 'exec'))
    return {"updated": True}
