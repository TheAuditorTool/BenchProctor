# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest48403(request: Request):
    referer_value = request.headers.get('referer', '')
    with open('/var/uploads/' + str(referer_value), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
