# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest78332(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
