# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def ensure_str(value):
    return str(value)

async def BenchmarkTest02469(request: Request):
    host_value = request.headers.get('host', '')
    data = ensure_str(host_value)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return {"updated": True}
