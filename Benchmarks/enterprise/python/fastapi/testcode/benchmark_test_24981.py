# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest24981(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    os.remove(str(data))
    return {"updated": True}
