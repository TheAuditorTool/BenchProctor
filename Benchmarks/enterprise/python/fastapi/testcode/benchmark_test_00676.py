# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from types import SimpleNamespace


async def BenchmarkTest00676(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        subprocess.run('echo ' + str(data), shell=True)
    await _evasion_task()
    return {"updated": True}
