# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest27149(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return {"updated": True}
