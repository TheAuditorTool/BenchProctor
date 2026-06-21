# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from urllib.parse import unquote


async def BenchmarkTest24079(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
