# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest18853(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
