# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest37350(request: Request, req: UserInput):
    json_value = req.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', json_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = json_value
    eval(str(processed))
    return {"updated": True}
