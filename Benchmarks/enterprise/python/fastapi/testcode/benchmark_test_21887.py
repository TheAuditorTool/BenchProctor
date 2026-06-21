# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import sys
from starlette.responses import JSONResponse
import asyncio


async def BenchmarkTest21887(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    async def fetch_payload():
        await asyncio.sleep(0)
        return argv_value
    data = await fetch_payload()
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
