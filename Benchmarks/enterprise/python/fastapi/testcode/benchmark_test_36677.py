# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36677(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
