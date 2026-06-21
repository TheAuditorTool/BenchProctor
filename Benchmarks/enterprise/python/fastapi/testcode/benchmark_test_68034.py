# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import asyncio
import socket


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest68034(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    async def _evasion_task():
        s = socket.create_connection((str(data), 80))
        s.close()
    await _evasion_task()
    return {"updated": True}
