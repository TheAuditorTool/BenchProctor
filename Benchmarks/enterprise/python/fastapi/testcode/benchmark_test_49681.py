# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest49681(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    request.session['user'] = str(data)
    return {"updated": True}
