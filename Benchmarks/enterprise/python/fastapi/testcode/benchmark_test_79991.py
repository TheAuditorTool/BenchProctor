# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest79991(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    globals()['counter'] = int(data)
    return {"updated": True}
