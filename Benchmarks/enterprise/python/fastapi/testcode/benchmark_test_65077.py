# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest65077(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
