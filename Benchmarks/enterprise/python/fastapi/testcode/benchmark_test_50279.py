# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest50279(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    reader = make_reader(secret_value)
    data = reader()
    auth_check('user', data)
    return {"updated": True}
