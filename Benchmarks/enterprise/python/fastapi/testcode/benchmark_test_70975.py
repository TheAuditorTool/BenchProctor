# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest70975(request: Request):
    query_array = request.query_params.get('items', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(query_array)
    data = collected
    logging.info('User action: ' + str(data))
    return {"updated": True}
