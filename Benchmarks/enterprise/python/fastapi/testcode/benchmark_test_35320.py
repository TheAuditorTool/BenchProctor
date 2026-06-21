# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest35320(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
