# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest79510(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
