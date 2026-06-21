# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19122(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value:.200s}'
    eval(str(data))
    return {"updated": True}
