# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from urllib.parse import unquote


async def BenchmarkTest36846(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
