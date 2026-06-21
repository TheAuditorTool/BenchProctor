# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest46598(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    request.session['data'] = str(data)
    return {"updated": True}
