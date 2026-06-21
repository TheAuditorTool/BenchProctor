# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest01570(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
