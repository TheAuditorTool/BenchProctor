# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest13222(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % str(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    exec(str(processed))
    return {"updated": True}
