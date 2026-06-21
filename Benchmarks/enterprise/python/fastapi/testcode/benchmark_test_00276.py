# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


def normalise_input(value):
    return value.strip()

async def BenchmarkTest00276(request: Request):
    referer_value = request.headers.get('referer', '')
    data = normalise_input(referer_value)
    if time.time() > 1000000000:
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
