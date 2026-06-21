# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest26782(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
