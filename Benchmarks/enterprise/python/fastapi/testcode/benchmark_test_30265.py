# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest30265(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
