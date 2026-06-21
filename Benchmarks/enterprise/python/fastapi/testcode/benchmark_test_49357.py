# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import re
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest49357(request: Request):
    referer_value = request.headers.get('referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return {"updated": True}
