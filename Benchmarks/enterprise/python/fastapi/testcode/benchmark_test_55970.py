# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest55970(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
