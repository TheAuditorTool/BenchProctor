# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01888(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
