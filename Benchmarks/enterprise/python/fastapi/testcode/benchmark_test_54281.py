# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from pydantic import BaseModel
import asyncio


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest54281(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return {"updated": True}
