# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08182(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
