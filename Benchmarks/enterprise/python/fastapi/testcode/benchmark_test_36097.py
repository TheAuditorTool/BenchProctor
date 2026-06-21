# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest36097(request: Request):
    ua_value = request.headers.get('user-agent', '')
    reader = make_reader(ua_value)
    data = reader()
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
