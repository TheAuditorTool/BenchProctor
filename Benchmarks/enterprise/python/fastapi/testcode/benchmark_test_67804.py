# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from starlette.responses import JSONResponse


async def BenchmarkTest67804(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
