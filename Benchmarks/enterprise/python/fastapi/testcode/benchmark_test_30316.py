# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest30316(request: Request):
    referer_value = request.headers.get('referer', '')
    reader = make_reader(referer_value)
    data = reader()
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
