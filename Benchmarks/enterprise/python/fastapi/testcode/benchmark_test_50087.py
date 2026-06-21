# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest50087(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    globals()['counter'] = int(data)
    return {"updated": True}
