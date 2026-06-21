# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from starlette.responses import JSONResponse


async def BenchmarkTest01353(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
