# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest04146(request: Request, req: UserInput):
    json_value = req.payload
    os.chmod('/var/app/data/' + str(json_value), 0o777)
    return {"updated": True}
