# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest59742(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
