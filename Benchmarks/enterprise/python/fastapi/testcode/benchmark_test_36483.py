# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from types import SimpleNamespace


async def BenchmarkTest36483(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
