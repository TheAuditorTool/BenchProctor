# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


async def BenchmarkTest52305(request: Request):
    user_id = request.query_params.get('id', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(user_id).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
