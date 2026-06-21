# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest23061(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
