# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import time


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest35692(request: Request, req: UserInput):
    json_value = req.payload
    data = '{}'.format(json_value)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
