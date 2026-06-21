# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest73341(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(multipart_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
