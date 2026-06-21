# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39853(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = str(header_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
