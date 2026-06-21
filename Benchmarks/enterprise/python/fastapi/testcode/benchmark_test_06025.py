# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest06025(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    reader = make_reader(header_value)
    data = reader()
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
