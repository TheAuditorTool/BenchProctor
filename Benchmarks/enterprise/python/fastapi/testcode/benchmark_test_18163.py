# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest18163(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
