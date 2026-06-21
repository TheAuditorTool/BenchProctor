# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest78621(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ' '.join(str(auth_header).split())
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
