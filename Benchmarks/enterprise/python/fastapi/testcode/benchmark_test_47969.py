# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from urllib.parse import unquote


async def BenchmarkTest47969(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
