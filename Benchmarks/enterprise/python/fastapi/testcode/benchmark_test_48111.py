# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest48111(request: Request):
    referer_value = request.headers.get('referer', '')
    reader = make_reader(referer_value)
    data = reader()
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
