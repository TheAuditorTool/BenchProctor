# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest03961(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    base_name = os.path.basename(str(cookie_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
