# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest02889(request: Request):
    auth_header = request.headers.get('authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
