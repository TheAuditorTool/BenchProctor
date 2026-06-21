# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest58620(request: Request):
    referer_value = request.headers.get('referer', '')
    logging.info('User action: ' + str(referer_value))
    return {"updated": True}
