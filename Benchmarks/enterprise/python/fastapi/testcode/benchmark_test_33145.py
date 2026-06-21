# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import pickle


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest33145(request: Request):
    referer_value = request.headers.get('referer', '')
    data = coalesce_blank(referer_value)
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    pickle.loads(processed.encode('latin-1'))
    return {"updated": True}
