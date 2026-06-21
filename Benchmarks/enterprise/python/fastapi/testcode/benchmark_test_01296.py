# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote


async def BenchmarkTest01296(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
