# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


async def BenchmarkTest17421(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = (lambda v: v.strip())(auth_header)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
