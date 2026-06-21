# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import asyncio
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest40507(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
