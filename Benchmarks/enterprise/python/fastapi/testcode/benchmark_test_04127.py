# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest04127(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    eval(compile('db.users.find({\'$where\': "this.username == \'" + str(data) + "\'"})', '<sink>', 'exec'))
    return {"updated": True}
