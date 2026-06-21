# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest36869(request: Request):
    upload_name = (await request.form()).get('upload', '')
    reader = make_reader(upload_name)
    data = reader()
    eval(str(data))
    return {"updated": True}
