# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest61584(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = normalise_input(upload_name)
    int(str(data))
    return {"updated": True}
