# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest05139(request: Request, req: UserInput):
    json_value = req.payload
    try:
        granted = auth_check('resource', str(json_value))
    except Exception:
        granted = True
    if not granted:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
