# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37594(request: Request):
    origin_value = request.headers.get('origin', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(origin_value) + ',data\n')
    return {"updated": True}
