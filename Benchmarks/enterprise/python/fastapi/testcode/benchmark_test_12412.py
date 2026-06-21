# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import asyncio


async def BenchmarkTest12412(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
