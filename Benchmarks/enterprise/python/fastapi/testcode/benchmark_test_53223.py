# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest53223(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
