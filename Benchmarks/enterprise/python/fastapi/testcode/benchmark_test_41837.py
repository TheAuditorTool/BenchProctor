# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest41837(request: Request):
    upload_name = (await request.form()).get('upload', '')
    importlib.import_module(str(upload_name))
    return {"updated": True}
