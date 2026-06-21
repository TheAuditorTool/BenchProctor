# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import runpy


async def BenchmarkTest12441(request: Request):
    path_value = request.path_params.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', path_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = path_value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
