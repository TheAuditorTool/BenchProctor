# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def ensure_str(value):
    return str(value)

async def BenchmarkTest11775(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ensure_str(origin_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
