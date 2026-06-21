# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest12121(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % (ua_value,)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
