# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
from urllib.parse import unquote


async def BenchmarkTest64549(request: Request):
    query_array = request.query_params.get('items', '')
    data = unquote(query_array)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
