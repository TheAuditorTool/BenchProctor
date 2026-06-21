# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45527(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
