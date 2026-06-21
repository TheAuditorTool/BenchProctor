# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from types import SimpleNamespace


async def BenchmarkTest05287(request: Request):
    upload_name = (await request.form()).get('upload', '')
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return {"updated": True}
