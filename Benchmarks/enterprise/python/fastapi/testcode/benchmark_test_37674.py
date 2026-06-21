# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest37674(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '{}'.format(header_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
