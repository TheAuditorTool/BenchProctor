# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest01712(request: Request):
    referer_value = request.headers.get('referer', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(referer_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
