# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest51564(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    reader = make_reader(header_value)
    data = reader()
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
