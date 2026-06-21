# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest79835(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
