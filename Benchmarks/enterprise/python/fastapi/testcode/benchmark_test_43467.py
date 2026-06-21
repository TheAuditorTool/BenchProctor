# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import asyncio


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest43467(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    if str(data).endswith(('/public', '/static', '/.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
