# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest52759(request: Request):
    ua_value = request.headers.get('user-agent', '')
    reader = make_reader(ua_value)
    data = reader()
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
