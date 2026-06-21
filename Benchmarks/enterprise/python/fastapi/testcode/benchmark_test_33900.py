# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form


async def BenchmarkTest33900(request: Request, field: str = Form('')):
    field_value = field
    logging.info('User action: ' + str(field_value))
    return {"updated": True}
