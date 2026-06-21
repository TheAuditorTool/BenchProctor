# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest79864(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
