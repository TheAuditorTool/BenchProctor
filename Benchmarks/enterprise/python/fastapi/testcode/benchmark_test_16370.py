# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from types import SimpleNamespace


async def BenchmarkTest16370(request: Request):
    path_value = request.path_params.get('id', '')
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return {"updated": True}
