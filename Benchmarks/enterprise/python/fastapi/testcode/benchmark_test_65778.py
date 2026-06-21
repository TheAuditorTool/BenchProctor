# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import urllib.request


async def BenchmarkTest65778(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
