# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest17375(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = default_blank(upload_name)
    request.session['user'] = str(data)
    return {"updated": True}
