# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi import Form
import asyncio


async def BenchmarkTest14449(request: Request, field: str = Form('')):
    field_value = field
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = await fetch_payload()
    processed = data[:64]
    return HTMLResponse('<div>' + str(processed) + '</div>')
