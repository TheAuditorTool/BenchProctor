# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse
import asyncio


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest02899(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JSONResponse({'token': str(token)}, status_code=200)
