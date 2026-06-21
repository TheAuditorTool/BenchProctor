# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest03692(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
