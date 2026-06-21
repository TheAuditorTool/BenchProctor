# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest40999(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
