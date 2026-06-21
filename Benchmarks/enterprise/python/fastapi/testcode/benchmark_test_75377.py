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

async def BenchmarkTest75377(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    processed = data[:64]
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
