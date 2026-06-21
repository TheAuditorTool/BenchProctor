# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest24491(request: Request):
    referer_value = request.headers.get('referer', '')
    data = (lambda v: v.strip())(referer_value)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
