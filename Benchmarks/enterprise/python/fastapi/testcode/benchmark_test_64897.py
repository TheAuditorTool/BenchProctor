# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest64897(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
