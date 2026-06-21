# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest21046(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
