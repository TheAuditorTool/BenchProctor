# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest10636(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
