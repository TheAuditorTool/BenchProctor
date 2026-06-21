# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest78288(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
