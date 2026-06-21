# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest11518(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
