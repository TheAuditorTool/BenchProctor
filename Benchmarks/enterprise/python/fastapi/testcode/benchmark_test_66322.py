# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
import asyncio


async def BenchmarkTest66322(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    async def _evasion_task():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    await _evasion_task()
    return {"updated": True}
