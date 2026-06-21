# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest31067(request: Request):
    referer_value = request.headers.get('referer', '')
    data = (lambda v: v.strip())(referer_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
