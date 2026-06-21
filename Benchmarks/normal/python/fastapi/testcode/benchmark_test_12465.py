# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest12465(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % (json_value,)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
