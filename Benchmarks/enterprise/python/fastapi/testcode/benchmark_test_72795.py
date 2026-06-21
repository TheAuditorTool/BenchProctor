# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest72795(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ensure_str(referer_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
