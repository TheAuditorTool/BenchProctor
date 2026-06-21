# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


async def BenchmarkTest42095(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
