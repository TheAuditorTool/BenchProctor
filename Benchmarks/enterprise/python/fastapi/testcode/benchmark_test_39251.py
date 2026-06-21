# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39251(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
