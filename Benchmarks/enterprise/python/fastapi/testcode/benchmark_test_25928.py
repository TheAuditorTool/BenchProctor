# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from types import SimpleNamespace


async def BenchmarkTest25928(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    json.loads(data)
    return {"updated": True}
