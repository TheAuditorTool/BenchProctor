# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest67502(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
