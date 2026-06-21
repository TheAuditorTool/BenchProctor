# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest42260(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JSONResponse({'error': 'file error'}, status_code=500)
    return {"updated": True}
