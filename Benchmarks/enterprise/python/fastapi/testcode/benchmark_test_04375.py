# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json


async def BenchmarkTest04375(request: Request):
    query_array = request.query_params.get('items', '')
    try:
        data = json.loads(query_array).get('value', query_array)
    except (json.JSONDecodeError, AttributeError):
        data = query_array
    logging.info('User action: ' + str(data))
    return {"updated": True}
