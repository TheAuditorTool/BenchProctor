# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse
import subprocess


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest32290(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
