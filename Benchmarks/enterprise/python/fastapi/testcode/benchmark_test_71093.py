# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


async def BenchmarkTest71093(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(forwarded_ip))
    return {"updated": True}
