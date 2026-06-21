# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
from fastapi import Form
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest59558(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
