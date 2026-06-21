# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest69007(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % str(ua_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
