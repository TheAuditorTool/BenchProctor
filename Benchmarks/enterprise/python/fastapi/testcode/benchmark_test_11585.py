# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest11585(request: Request):
    origin_value = request.headers.get('origin', '')
    data = default_blank(origin_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
