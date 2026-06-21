# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest38418(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
