# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest14709(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    logging.info('User action: ' + str(data))
    return {"updated": True}
