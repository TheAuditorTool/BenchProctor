# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest64559(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
