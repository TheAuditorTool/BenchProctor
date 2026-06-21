# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest08584(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    logging.info('User action: ' + str(data))
    return {"updated": True}
