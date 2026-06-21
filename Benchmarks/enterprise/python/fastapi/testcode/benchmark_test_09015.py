# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from urllib.parse import unquote


async def BenchmarkTest09015(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
