# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from pydantic import BaseModel
from starlette.responses import JSONResponse
import os


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest72617(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
