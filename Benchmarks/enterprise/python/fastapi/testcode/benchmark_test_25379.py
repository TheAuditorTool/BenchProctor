# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest25379(request: Request):
    upload_name = (await request.form()).get('upload', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    request.session['data'] = str(data)
    return {"updated": True}
