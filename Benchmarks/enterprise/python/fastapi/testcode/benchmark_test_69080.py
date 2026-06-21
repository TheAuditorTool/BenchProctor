# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import asyncio


async def BenchmarkTest69080(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = await fetch_payload()
    _ev = {}
    eval(compile('_ev[\'r\'] = HTMLResponse(\'<script src="\' + str(data) + \'"></script>\')', '<sink>', 'exec'))
    return _ev['r']
