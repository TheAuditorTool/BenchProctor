# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import pickle


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest04755(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value}'
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
