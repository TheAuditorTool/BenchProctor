# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56214(request: Request):
    referer_value = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
