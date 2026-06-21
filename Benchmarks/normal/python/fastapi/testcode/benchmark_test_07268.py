# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest07268(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
