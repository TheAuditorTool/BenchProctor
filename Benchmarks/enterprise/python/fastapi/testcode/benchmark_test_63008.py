# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import runpy


async def BenchmarkTest63008(request: Request):
    host_value = request.headers.get('host', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', host_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = host_value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
