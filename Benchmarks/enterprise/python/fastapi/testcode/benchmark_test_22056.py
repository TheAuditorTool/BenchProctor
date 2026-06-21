# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest22056(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return {"updated": True}
