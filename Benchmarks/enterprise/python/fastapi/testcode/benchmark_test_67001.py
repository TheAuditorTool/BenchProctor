# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment
import asyncio


async def BenchmarkTest67001(request: Request):
    user_id = request.query_params.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = await fetch_payload()
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
