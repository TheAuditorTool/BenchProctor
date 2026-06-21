# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import asyncio


async def BenchmarkTest28605(request: Request):
    referer_value = request.headers.get('referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = await fetch_payload()
    _ev = {}
    eval(compile('_ev[\'r\'] = HTMLResponse(\'<script src="\' + str(data) + \'"></script>\')', '<sink>', 'exec'))
    return _ev['r']
