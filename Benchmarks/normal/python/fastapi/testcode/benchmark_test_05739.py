# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from fastapi import Form


async def BenchmarkTest05739(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
