# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


async def BenchmarkTest71818(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '{}'.format(xml_value)
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
