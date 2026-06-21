# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from urllib.parse import unquote


async def BenchmarkTest00444(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
