# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest53878(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    os.remove(str(data))
    return {"updated": True}
