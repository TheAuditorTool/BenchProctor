# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import importlib


async def BenchmarkTest04463(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '%s' % str(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    importlib.import_module(str(processed))
    return {"updated": True}
