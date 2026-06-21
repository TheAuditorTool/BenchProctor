# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest68887(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value}'
    return RedirectResponse(url=str(data))
