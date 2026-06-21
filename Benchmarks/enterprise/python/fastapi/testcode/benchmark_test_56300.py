# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest56300(request: Request, req: UserInput):
    json_value = req.payload
    allowed = {'config.json', 'index.html', 'readme.md'}
    if json_value not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + json_value
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
