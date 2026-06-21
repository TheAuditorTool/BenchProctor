# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import pickle


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest01666(request: Request, req: UserInput):
    json_value = req.payload
    if json_value:
        data = json_value
    else:
        data = ''
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
