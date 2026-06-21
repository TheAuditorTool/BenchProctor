# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import os
import asyncio


async def BenchmarkTest43057(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = await fetch_payload()
    if os.environ.get("APP_ENV", "production") != "test":
        return RedirectResponse(url=str(data))
    return {"updated": True}
