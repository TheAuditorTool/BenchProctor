# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import importlib


async def BenchmarkTest80885(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
