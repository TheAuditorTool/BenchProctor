# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest20900(request: Request):
    auth_header = request.headers.get('authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
