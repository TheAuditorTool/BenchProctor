# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import tempfile


async def BenchmarkTest13006(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
