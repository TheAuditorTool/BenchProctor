# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import JSONResponse
import runpy


@dataclass
class FormData:
    payload: str

async def BenchmarkTest03129(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
