# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest66070(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
