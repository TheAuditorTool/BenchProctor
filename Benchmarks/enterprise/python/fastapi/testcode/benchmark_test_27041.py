# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest27041(request: Request, req: UserInput):
    json_value = req.payload
    data = default_blank(json_value)
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
