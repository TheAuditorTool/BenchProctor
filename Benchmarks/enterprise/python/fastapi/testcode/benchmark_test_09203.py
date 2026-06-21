# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest09203(request: Request):
    query_array = request.query_params.get('items', '')
    data = default_blank(query_array)
    logging.info('User action: ' + str(data))
    return {"updated": True}
