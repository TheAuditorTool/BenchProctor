# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest18738(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = header_value if header_value else 'default'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
