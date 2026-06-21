# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest27712(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
