# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest51237(request):
    cookie_value = request.COOKIES.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
