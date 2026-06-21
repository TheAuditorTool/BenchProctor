# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


async def BenchmarkTest34974(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
