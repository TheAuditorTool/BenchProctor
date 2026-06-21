# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from urllib.parse import unquote


async def BenchmarkTest46525(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    globals()['counter'] = int(data)
    return {"updated": True}
