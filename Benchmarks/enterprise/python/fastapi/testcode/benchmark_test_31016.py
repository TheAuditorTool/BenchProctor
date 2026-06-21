# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from types import SimpleNamespace


async def BenchmarkTest31016(request: Request):
    host_value = request.headers.get('host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return {"updated": True}
