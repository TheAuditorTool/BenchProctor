# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
from app_runtime import auth_check


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest28137(request: Request, req: UserInput):
    json_value = req.payload
    if not auth_check(request.session.get('user', ''), str(json_value)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
