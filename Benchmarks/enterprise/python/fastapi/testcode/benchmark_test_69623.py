# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest69623(request: Request):
    origin_value = request.headers.get('origin', '')
    base_name = os.path.basename(str(origin_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
