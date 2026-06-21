# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse
import json
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest34006(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.environ['APP_USER_PREFERENCE'] = str(processed)
    return JSONResponse({'config_set': 'APP_USER_PREFERENCE'}, status_code=200)
