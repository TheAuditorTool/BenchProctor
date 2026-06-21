# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest08783(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value}'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
