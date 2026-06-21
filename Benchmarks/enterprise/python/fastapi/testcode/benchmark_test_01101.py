# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01101(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
