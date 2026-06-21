# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest22905(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
