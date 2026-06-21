# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


async def BenchmarkTest16841(request: Request):
    referer_value = request.headers.get('referer', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(referer_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
