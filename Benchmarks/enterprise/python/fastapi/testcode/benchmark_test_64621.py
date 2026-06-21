# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse


async def BenchmarkTest64621(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', xml_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = xml_value
    os.system('echo ' + str(processed))
    return {"updated": True}
