# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest56457(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
