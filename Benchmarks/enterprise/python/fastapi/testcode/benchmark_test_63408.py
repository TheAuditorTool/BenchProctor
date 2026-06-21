# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import socket


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest63408(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
