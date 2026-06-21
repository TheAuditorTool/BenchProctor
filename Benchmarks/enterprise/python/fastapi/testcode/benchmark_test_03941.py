# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest03941(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ' '.join(str(referer_value).split())
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
