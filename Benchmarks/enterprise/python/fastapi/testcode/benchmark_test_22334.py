# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22334(request: Request):
    path_value = request.path_params.get('id', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(path_value))
    return {"updated": True}
