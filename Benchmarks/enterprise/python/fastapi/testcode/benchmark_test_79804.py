# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import asyncio


async def BenchmarkTest79804(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
