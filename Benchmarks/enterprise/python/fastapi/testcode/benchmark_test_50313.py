# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest50313(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
