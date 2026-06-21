# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest08769(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    reader = make_reader(header_value)
    data = reader()
    os.remove(str(data))
    return {"updated": True}
