# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest74130(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % str(path_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
