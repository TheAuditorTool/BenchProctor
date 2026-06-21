# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re


def ensure_str(value):
    return str(value)

async def BenchmarkTest75345(request: Request):
    user_id = request.query_params.get('id', '')
    data = ensure_str(user_id)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
