# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import base64


async def BenchmarkTest68017(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
