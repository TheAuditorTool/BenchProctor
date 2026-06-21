# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest05811(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    return HTMLResponse('<div>' + str(data) + '</div>')
