# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest75717(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
