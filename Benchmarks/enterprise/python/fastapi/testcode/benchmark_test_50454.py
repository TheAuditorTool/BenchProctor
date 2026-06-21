# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest50454(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ' '.join(str(raw_body).split())
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
