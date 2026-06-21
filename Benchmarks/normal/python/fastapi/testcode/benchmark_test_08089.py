# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest08089(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
