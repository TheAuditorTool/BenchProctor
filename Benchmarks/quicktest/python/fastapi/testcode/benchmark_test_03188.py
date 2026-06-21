# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest03188(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
