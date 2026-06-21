# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest57204(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
