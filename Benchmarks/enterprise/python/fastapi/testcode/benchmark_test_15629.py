# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import importlib


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest15629(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
