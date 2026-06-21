# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest64455(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = (lambda v: v.strip())(header_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
