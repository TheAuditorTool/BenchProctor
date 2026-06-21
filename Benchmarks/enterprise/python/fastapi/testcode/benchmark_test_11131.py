# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11131(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
