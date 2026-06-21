# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import os


async def BenchmarkTest27596(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
