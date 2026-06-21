# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67845(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
