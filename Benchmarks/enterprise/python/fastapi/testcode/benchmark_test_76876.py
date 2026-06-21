# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from starlette.responses import JSONResponse


async def BenchmarkTest76876(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = str(header_value).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
