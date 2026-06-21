# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from fastapi import Form
import asyncio


async def BenchmarkTest17784(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
