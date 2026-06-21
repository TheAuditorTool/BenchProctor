# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest79917(request: Request):
    ua_value = request.headers.get('user-agent', '')
    with open('/var/uploads/' + str(ua_value), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
