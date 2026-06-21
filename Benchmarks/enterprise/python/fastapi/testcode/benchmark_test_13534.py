# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse


async def BenchmarkTest13534(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
