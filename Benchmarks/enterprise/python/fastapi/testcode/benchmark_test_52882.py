# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import base64


async def BenchmarkTest52882(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    logging.info('User action: ' + str(data))
    return {"updated": True}
