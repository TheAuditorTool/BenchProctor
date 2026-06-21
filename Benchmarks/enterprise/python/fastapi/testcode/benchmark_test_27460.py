# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from types import SimpleNamespace


async def BenchmarkTest27460(request: Request):
    query_array = request.query_params.get('items', '')
    ns = SimpleNamespace(payload=query_array)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return {"updated": True}
