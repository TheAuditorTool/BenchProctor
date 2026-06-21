# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest63438(request: Request, req: UserInput):
    json_value = req.payload
    if json_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = json_value
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
