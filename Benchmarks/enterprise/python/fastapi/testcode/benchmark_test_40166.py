# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest40166(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    requests.get(str(data))
    return {"updated": True}
