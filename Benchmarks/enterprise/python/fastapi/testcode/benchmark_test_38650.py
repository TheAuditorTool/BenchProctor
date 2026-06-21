# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest38650(request: Request, req: UserInput):
    json_value = req.payload
    reader = make_reader(json_value)
    data = reader()
    os.system('echo ' + str(data))
    return {"updated": True}
