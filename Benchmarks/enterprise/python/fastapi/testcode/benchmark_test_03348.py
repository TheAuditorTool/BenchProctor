# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest03348(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
