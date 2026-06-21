# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest48761(request: Request):
    host_value = request.headers.get('host', '')
    reader = make_reader(host_value)
    data = reader()
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
