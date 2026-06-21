# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest20937(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value:.200s}'
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
