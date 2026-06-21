# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
import importlib


def normalise_input(value):
    return value.strip()

async def BenchmarkTest01122(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
