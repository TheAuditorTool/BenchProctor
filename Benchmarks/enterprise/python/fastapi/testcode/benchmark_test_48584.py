# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import importlib


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest48584(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
