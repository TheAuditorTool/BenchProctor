# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import asyncio


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest44898(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
