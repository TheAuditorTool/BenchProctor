# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest12048(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = normalise_input(upload_name)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
