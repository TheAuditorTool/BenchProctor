# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest24530(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
