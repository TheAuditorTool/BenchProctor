# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest40955(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
