# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form


async def BenchmarkTest00185(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
