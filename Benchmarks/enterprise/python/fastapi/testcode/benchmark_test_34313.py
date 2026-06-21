# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest34313(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
