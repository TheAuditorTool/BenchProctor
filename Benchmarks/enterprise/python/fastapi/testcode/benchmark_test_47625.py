# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import pickle


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest47625(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
