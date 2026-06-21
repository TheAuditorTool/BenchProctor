# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest73220(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
