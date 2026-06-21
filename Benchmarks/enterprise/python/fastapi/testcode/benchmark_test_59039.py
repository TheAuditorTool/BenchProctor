# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


async def BenchmarkTest59039(request: Request):
    origin_value = request.headers.get('origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
