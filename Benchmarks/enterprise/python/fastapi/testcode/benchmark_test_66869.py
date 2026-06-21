# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest66869(request: Request):
    referer_value = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
