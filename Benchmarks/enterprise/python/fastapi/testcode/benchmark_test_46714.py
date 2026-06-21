# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest46714(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    parts = []
    for token in str(argv_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
