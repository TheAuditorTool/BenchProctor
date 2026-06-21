# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest56902(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    return HTMLResponse('<script src="' + str(data) + '"></script>')
