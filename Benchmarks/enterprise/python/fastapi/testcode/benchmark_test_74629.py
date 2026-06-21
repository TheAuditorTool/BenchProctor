# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest74629(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
