# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest39436(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    with open(os.path.join('/var/app/data', str(header_value)), 'r') as fh:
        content = fh.read()
    return content
