# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import os
import asyncio


async def BenchmarkTest51962(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse(Template(data).render())
    return {"updated": True}
