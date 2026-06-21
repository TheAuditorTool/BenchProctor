# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest52660(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value}'
    os.remove(str(data))
    return {"updated": True}
