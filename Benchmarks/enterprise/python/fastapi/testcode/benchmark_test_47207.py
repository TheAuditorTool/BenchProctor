# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest47207(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value}'
    globals()['counter'] = int(data)
    return {"updated": True}
