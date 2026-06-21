# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from types import SimpleNamespace


async def BenchmarkTest49188(request: Request):
    query_array = request.query_params.get('items', '')
    ns = SimpleNamespace(payload=query_array)
    data = getattr(ns, 'payload')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
