# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def relay_value(value):
    return value

async def BenchmarkTest70396(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = relay_value(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return {"updated": True}
