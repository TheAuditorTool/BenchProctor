# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest16820(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '{}'.format(raw_body)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
