# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import asyncio


async def BenchmarkTest02682(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return {"updated": True}
