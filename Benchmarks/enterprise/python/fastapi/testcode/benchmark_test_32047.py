# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest32047(request: Request, req: UserInput):
    json_value = req.payload
    try:
        os.setuid(int(str(json_value)) if str(json_value).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
