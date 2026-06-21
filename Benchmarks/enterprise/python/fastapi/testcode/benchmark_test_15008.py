# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest15008(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
