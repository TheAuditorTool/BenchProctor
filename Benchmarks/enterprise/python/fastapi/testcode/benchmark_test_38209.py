# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest38209(request: Request):
    origin_value = request.headers.get('origin', '')
    data = coalesce_blank(origin_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
