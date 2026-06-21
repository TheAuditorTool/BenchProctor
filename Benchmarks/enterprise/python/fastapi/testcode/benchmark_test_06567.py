# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


async def BenchmarkTest06567(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
