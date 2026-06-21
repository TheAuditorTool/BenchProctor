# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import asyncio


async def BenchmarkTest02492(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = await fetch_payload()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
