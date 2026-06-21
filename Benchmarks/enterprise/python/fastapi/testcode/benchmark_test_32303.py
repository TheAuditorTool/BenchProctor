# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest32303(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    try:
        result = int(str(data))
    except ValueError as e:
        return JSONResponse({'error': str(e)}, status_code=400)
    return {"updated": True}
