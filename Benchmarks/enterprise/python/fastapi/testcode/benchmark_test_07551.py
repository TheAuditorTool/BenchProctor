# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest07551(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    os.chmod('/var/app/data/' + str(cookie_value), 0o777)
    return {"updated": True}
