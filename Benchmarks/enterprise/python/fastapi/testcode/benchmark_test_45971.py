# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest45971(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '{}'.format(raw_body)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
