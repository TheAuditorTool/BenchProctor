# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76871(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    eval(str(data))
    return {"updated": True}
