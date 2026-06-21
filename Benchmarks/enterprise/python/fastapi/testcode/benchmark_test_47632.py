# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
from starlette.responses import HTMLResponse


async def BenchmarkTest47632(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    return HTMLResponse('<script src="' + str(data) + '"></script>')
