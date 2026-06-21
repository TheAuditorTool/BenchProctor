# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from starlette.responses import JSONResponse


async def BenchmarkTest57793(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', forwarded_ip):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = forwarded_ip
    logging.info('User action: ' + str(processed))
    return {"updated": True}
