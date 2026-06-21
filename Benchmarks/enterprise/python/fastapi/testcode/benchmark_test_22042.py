# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from urllib.parse import unquote


async def BenchmarkTest22042(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
