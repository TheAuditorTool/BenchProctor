# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53623(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(header_value) + ',data\n')
    return {"updated": True}
