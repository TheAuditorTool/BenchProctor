# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import runpy


async def BenchmarkTest69301(request: Request):
    origin_value = request.headers.get('origin', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', origin_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = origin_value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
