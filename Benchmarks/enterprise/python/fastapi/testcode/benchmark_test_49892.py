# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest49892(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % str(raw_body)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
