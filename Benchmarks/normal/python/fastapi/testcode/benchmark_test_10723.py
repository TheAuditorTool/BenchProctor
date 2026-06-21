# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import json
import re


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest10723(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JSONResponse({'validated': str(processed)}, status_code=200)
    return {"updated": True}
