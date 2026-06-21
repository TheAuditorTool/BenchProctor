# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest39091(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    logging.info('User action: ' + str(data))
    return {"updated": True}
