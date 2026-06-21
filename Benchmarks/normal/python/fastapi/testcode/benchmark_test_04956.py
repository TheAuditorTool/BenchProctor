# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest04956(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = handle(upload_name)
    eval(compile("db.execute('SELECT * FROM users WHERE id = ' + str(data))", '<sink>', 'exec'))
    return {"updated": True}
