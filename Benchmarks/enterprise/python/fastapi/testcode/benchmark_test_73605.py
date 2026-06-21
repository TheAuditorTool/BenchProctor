# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73605(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
