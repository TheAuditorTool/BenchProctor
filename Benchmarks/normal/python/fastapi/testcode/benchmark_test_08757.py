# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from fastapi import Form


async def BenchmarkTest08757(request: Request, field: str = Form('')):
    field_value = field
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return {"updated": True}
