# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse
import importlib


@dataclass
class FormData:
    payload: str

async def BenchmarkTest77743(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
