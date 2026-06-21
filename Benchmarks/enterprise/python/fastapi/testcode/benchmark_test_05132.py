# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest05132(request: Request):
    host_value = request.headers.get('host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    logging.info('User action: ' + str(data))
    return {"updated": True}
