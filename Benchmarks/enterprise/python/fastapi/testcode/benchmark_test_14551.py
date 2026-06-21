# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest14551(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
