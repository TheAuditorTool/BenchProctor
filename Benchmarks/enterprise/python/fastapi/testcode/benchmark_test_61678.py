# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import asyncio


async def BenchmarkTest61678(request: Request):
    host_value = request.headers.get('host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = await fetch_payload()
    _ev = {}
    eval(compile('_ev[\'r\'] = HTMLResponse(\'<script src="\' + str(data) + \'"></script>\')', '<sink>', 'exec'))
    return _ev['r']
