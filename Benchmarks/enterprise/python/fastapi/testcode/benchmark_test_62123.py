# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from types import SimpleNamespace


async def BenchmarkTest62123(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return {"updated": True}
