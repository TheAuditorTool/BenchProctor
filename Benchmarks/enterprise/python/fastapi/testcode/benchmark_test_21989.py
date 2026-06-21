# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import json


async def BenchmarkTest21989(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
