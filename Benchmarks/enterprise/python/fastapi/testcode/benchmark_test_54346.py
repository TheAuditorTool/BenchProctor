# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest54346(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
