# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


async def BenchmarkTest63294(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
