# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from pydantic import BaseModel
import asyncio


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest66177(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    _ev = {}
    eval(compile('_ev[\'r\'] = HTMLResponse(\'<img src="\' + str(data) + \'">\')', '<sink>', 'exec'))
    return _ev['r']
