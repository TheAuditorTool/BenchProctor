# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


def normalise_input(value):
    return value.strip()

async def BenchmarkTest34938(request: Request):
    host_value = request.headers.get('host', '')
    data = normalise_input(host_value)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return {"updated": True}
