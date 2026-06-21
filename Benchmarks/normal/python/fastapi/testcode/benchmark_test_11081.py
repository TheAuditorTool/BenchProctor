# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
from fastapi import Form


async def BenchmarkTest11081(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
