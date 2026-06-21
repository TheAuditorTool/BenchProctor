# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from starlette.responses import JSONResponse


async def BenchmarkTest41485(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
