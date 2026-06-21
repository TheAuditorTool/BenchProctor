# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import asyncio


async def BenchmarkTest21936(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    _ev = {}
    eval(compile("_ev['r'] = HTMLResponse(Template(data).render())", '<sink>', 'exec'))
    return _ev['r']
