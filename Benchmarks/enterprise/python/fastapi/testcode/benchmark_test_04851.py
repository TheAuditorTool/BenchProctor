# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04851(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
