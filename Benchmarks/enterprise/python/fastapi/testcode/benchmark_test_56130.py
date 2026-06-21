# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import json


async def BenchmarkTest56130(request: Request):
    query_array = request.query_params.get('items', '')
    try:
        data = json.loads(query_array).get('value', query_array)
    except (json.JSONDecodeError, AttributeError):
        data = query_array
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return {"updated": True}
