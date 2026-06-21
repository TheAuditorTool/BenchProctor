# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import asyncio
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest47783(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
