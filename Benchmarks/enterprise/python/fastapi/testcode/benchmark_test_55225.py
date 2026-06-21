# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time
from types import SimpleNamespace


async def BenchmarkTest55225(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
