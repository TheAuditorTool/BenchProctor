# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest62473(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
