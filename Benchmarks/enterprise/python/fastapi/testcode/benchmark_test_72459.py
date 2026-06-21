# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest72459(request: Request, field: str = Form('')):
    field_value = field
    if field_value not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = field_value
    os.system('echo ' + str(processed))
    return {"updated": True}
