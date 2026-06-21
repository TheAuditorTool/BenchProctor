# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest33238(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    processed = shlex.quote(forwarded_ip)
    os.system('echo ' + str(processed))
    return {"updated": True}
