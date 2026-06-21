# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def to_text(value):
    return str(value).strip()

async def BenchmarkTest56078(request: Request, req: UserInput):
    json_value = req.payload
    data = to_text(json_value)
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
