# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import json
import asyncio


async def BenchmarkTest80669(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = await fetch_payload()
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
