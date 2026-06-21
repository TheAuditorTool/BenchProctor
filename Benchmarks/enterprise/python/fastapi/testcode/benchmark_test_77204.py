# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import os
from starlette.responses import JSONResponse
import runpy


def to_text(value):
    return str(value).strip()

async def BenchmarkTest77204(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
