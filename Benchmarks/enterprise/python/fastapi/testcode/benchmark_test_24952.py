# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest24952(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
