# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest30791(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
