# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest42004(request: Request, req: UserInput):
    json_value = req.payload
    os.setuid(int(str(json_value)) if str(json_value).isdigit() else 0)
    return {"updated": True}
