# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest57319(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value:.200s}'
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
