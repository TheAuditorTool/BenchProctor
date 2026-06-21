# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59928(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
