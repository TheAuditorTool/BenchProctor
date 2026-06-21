# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest10269(request: Request):
    origin_value = request.headers.get('origin', '')
    processed = shlex.quote(origin_value)
    os.system('echo ' + str(processed))
    return {"updated": True}
