# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest10736(request: Request):
    referer_value = request.headers.get('referer', '')
    base_name = os.path.basename(str(referer_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
