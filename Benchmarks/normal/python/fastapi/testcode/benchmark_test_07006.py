# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import asyncio


async def BenchmarkTest07006(request: Request):
    upload_name = (await request.form()).get('upload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = await fetch_payload()
    _ev = {}
    eval(compile("_ev['r'] = HTMLResponse(Template(data).render())", '<sink>', 'exec'))
    return _ev['r']
