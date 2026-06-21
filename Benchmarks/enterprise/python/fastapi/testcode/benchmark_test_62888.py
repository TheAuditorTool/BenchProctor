# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form


async def BenchmarkTest62888(request: Request, field: str = Form('')):
    field_value = field
    processed = 'true' if str(field_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
