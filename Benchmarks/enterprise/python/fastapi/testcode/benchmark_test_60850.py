# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest60850(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    globals()['counter'] = int(data)
    return {"updated": True}
