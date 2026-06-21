# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11681(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
