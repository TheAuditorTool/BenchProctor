# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest47919(request: Request, req: UserInput):
    json_value = req.payload
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
