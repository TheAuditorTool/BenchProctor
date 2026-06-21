# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest15496(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
