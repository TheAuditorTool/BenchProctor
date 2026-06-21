# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse
import subprocess


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest03815(request: Request, req: UserInput):
    json_value = req.payload
    kind = 'json' if str(json_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = json_value
            data = parsed
        case _:
            data = json_value
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
