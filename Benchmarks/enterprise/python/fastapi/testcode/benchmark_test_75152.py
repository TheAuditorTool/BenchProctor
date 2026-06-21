# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest75152(request: Request):
    referer_value = request.headers.get('referer', '')
    data = to_text(referer_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
