# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from types import SimpleNamespace


async def BenchmarkTest68131(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
