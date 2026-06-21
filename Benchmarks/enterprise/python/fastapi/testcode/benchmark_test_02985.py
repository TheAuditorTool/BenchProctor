# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form


async def BenchmarkTest02985(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    logging.info('User action: ' + str(data))
    return {"updated": True}
