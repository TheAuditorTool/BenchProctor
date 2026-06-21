# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''
def ensure_str(value):
    return str(value)

async def BenchmarkTest29499(request: Request, req: UserInput):
    json_value = req.payload
    data = ensure_str(json_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse('<img src="' + str(data) + '">')
    return {"updated": True}
