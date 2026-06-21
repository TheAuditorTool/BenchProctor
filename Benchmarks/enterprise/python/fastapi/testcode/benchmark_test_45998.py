# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


async def BenchmarkTest45998(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
