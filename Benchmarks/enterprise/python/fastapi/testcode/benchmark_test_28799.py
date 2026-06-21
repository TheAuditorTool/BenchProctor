# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest28799(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
