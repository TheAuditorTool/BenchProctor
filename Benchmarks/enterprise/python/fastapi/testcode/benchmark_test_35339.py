# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest35339(request: Request, req: UserInput):
    json_value = req.payload
    if not str(json_value).isdigit():
        raise ValueError('invalid input: ' + str(json_value))
    return {"updated": True}
