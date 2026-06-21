# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest10427(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
