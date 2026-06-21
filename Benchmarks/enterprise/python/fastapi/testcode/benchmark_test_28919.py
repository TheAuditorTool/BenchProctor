# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import runpy


async def BenchmarkTest28919(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', xml_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = xml_value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
