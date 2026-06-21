# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43765(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
