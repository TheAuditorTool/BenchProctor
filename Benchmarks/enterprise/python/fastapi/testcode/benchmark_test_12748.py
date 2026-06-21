# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest12748(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = header_value if header_value else 'default'
    os.remove(str(data))
    return {"updated": True}
