# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def relay_value(value):
    return value

async def BenchmarkTest28816(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = relay_value(raw_body)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
