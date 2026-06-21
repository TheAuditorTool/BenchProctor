# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest51379(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    globals()['counter'] = int(data)
    return {"updated": True}
