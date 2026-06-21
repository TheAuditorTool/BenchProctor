# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import importlib


def to_text(value):
    return str(value).strip()

async def BenchmarkTest27020(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = to_text(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
