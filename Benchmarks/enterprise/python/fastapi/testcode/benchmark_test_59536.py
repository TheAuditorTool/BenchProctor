# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form


async def BenchmarkTest59536(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
