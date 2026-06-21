# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import json
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest80730(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
