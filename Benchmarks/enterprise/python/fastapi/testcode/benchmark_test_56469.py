# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
import asyncio


async def BenchmarkTest56469(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = await fetch_payload()
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
