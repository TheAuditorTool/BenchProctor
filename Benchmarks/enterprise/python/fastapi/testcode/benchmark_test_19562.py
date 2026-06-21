# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19562(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
