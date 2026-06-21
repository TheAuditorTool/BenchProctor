# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20552(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if not str(header_value).isdigit():
        raise Exception('error: ' + str(header_value))
    return {"updated": True}
