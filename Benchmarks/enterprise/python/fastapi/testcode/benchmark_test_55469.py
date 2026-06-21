# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest55469(request: Request):
    origin_value = request.headers.get('origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
