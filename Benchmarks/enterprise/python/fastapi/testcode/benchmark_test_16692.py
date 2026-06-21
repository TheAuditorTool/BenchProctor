# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


def normalise_input(value):
    return value.strip()

async def BenchmarkTest16692(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = normalise_input(header_value)
    processed = data[:64]
    conn = ldap.initialize('ldap://localhost:389')
    conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(processed))
    return {"updated": True}
