# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest61949(request: Request):
    origin_value = request.headers.get('origin', '')
    reader = make_reader(origin_value)
    data = reader()
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
