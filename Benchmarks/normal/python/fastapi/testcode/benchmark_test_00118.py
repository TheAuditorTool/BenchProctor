# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest00118(request: Request):
    ua_value = request.headers.get('user-agent', '')
    reader = make_reader(ua_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
