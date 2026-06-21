# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os
import asyncio


async def BenchmarkTest02134(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    async def _evasion_task():
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return await _evasion_task()
