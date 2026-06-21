# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest78452(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip}'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return {"updated": True}
