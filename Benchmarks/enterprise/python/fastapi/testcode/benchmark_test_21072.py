# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import asyncio


async def BenchmarkTest21072(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
