# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from types import SimpleNamespace


async def BenchmarkTest70042(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
