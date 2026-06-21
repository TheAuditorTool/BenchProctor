# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest20131(request: Request):
    referer_value = request.headers.get('referer', '')
    with open(os.path.join('/var/app/data', str(referer_value)), 'r') as fh:
        content = fh.read()
    return content
