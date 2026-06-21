# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from types import SimpleNamespace


async def BenchmarkTest63641(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    ns = SimpleNamespace(payload=prop_value)
    data = getattr(ns, 'payload')
    logging.info('User action: ' + str(data))
    return {"updated": True}
