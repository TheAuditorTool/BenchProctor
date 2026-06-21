# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest77599(request: Request, req: UserInput):
    json_value = req.payload
    base_name = os.path.basename(str(json_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
