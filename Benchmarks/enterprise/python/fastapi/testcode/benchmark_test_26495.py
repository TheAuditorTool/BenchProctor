# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest26495(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % (path_value,)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
