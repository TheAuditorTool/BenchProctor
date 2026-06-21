# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest66063(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
