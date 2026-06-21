# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel
from starlette.responses import JSONResponse
import subprocess


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest05882(request: Request, req: UserInput):
    json_value = req.payload
    if json_value not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = json_value
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
