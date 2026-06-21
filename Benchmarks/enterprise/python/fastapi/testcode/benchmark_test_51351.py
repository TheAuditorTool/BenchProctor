# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest51351(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = argv_value if argv_value else 'default'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.unlink('/var/app/data/' + str(processed))
    return {"updated": True}
