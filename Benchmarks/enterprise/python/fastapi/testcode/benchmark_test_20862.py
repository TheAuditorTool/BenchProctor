# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20862(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
