# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel
import asyncio


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest19591(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
