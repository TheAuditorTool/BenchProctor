# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex
from types import SimpleNamespace


async def BenchmarkTest53072(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
