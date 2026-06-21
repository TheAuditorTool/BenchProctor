# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import socket


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest31334(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
