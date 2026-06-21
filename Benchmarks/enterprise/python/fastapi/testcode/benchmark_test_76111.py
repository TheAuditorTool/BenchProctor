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

async def BenchmarkTest76111(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    def _primary():
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
