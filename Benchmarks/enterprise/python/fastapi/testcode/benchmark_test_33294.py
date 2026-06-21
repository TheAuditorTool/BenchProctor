# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33294(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
