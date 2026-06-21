# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10640(request: Request):
    referer_value = request.headers.get('referer', '')
    data = referer_value if referer_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
