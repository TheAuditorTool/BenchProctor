# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest14198(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
