# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form


async def BenchmarkTest05732(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return {"updated": True}
