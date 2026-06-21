# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import sys


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest71914(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    reader = make_reader(argv_value)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
