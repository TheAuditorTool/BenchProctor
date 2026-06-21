# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


async def BenchmarkTest00264(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
