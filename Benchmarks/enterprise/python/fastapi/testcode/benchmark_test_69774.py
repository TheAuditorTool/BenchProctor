# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest69774(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
