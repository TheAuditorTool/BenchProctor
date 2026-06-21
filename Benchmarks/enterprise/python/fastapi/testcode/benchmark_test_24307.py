# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest24307(request: Request):
    host_value = request.headers.get('host', '')
    reader = make_reader(host_value)
    data = reader()
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
