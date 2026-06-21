# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest52699(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
