# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import asyncio


async def BenchmarkTest02448(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = await fetch_payload()
    _ev = {}
    eval(compile("_ev['r'] = RedirectResponse(url=str(data))", '<sink>', 'exec'))
    return _ev['r']
