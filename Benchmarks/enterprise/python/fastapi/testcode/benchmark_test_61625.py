# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61625(request: Request):
    origin_value = request.headers.get('origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
