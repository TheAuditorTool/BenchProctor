# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import re
from starlette.responses import JSONResponse
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest38519(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\[\\]\'\\"=_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
