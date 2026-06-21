# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def relay_value(value):
    return value

async def BenchmarkTest48610(request: Request):
    origin_value = request.headers.get('origin', '')
    data = relay_value(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
