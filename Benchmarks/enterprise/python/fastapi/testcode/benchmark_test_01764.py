# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest01764(request: Request):
    upload_name = (await request.form()).get('upload', '')
    reader = make_reader(upload_name)
    data = reader()
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return {"updated": True}
