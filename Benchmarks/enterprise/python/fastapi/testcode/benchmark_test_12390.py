# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import runpy


async def BenchmarkTest12390(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', header_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = header_value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
