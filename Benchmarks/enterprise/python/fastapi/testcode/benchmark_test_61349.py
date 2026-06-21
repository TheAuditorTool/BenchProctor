# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest61349(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = default_blank(header_value)
    if os.environ.get("APP_ENV", "production") != "test":
        conn = ldap.initialize('ldap://localhost:389')
        conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))
    return {"updated": True}
