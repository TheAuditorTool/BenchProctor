# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os
import asyncio


async def BenchmarkTest05393(request: Request):
    path_value = request.path_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = await fetch_payload()
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
