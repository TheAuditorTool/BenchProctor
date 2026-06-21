# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest00599(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = default_blank(multipart_value)
    eval(compile("conn = ldap.initialize('ldap://localhost:389')\nconn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))", '<sink>', 'exec'))
    return {"updated": True}
