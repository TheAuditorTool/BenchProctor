# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import asyncio


async def BenchmarkTest74903(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
