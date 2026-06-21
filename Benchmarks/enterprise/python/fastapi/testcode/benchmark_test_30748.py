# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest30748(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    async def _evasion_task():
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    await _evasion_task()
    return {"updated": True}
