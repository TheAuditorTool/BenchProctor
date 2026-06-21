# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from urllib.parse import unquote


async def BenchmarkTest29321(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    logging.info('User action: ' + str(data))
    return {"updated": True}
