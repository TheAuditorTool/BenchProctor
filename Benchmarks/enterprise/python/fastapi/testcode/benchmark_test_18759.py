# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest18759(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
