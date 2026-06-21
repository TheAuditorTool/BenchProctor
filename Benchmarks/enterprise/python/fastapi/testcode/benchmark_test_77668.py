# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77668(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    eval(str(header_value))
    return {"updated": True}
