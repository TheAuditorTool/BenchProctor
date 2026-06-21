# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest40206(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(header_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
