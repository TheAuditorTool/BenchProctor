# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest20679(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
