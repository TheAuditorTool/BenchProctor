# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest26686(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
