# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11706(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    int(str(data))
    return {"updated": True}
