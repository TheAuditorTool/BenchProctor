# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from urllib.parse import unquote


async def BenchmarkTest01961(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
