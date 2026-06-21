# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest25095(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
