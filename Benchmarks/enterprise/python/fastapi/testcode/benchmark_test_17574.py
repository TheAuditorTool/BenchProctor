# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import runpy


async def BenchmarkTest17574(request: Request):
    auth_header = request.headers.get('authorization', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', auth_header):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = auth_header
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
