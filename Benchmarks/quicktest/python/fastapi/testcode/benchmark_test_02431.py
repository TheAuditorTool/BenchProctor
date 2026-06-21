# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest02431(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    auth_check('user', data)
    return {"updated": True}
