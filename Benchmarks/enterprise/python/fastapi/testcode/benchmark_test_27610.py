# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ldap


def relay_value(value):
    return value

async def BenchmarkTest27610(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = relay_value(multipart_value)
    eval(compile("conn = ldap.initialize('ldap://localhost:389')\nconn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, 'uid=' + str(data))", '<sink>', 'exec'))
    return {"updated": True}
