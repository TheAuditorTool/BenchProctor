# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest65247(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
