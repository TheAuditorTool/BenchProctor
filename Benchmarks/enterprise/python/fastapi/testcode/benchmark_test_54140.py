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

async def BenchmarkTest54140(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    processed = data[:64]
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
