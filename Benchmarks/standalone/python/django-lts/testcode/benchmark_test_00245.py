# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import defusedxml.ElementTree
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00245(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    for _event, element in defusedxml.ElementTree.iterparse(io.BytesIO(str(data).encode()), events=('end',)):
        element.clear()
    return JsonResponse({"saved": True})
