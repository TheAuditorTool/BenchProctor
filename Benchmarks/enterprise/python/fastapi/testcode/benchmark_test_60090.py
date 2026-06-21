# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest60090(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = normalise_input(upload_name)
    os.remove(str(data))
    return {"updated": True}
