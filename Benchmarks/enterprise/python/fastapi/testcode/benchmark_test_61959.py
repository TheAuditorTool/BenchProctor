# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61959(request: Request):
    referer_value = request.headers.get('referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
