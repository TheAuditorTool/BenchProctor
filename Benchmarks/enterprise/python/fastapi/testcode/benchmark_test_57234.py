# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest57234(request: Request, req: UserInput):
    json_value = req.payload
    return RedirectResponse(url=str(json_value))
