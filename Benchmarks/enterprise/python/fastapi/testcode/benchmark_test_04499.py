# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import tempfile


async def BenchmarkTest04499(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
