# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel
import asyncio


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest18438(request: Request, req: UserInput):
    json_value = req.payload
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = await fetch_payload()
    checked_path = os.path.normpath(data)
    link_path = os.path.join('/var/app/data', str(checked_path))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
