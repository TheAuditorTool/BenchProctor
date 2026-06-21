# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest01909(request: Request):
    upload_name = (await request.form()).get('upload', '')
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
