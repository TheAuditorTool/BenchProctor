# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest46510(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return JSONResponse({'error': 'privilege drop failed'}, status_code=500)
    return {"updated": True}
