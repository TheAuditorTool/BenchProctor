# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import sys
from types import SimpleNamespace


async def BenchmarkTest31842(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    ns = SimpleNamespace(payload=argv_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
