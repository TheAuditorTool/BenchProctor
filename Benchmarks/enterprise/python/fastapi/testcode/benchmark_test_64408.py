# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64408(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if not str(header_value).isdigit():
        raise ValueError('invalid input: ' + str(header_value))
    return {"updated": True}
