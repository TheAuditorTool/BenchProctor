# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest40494(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
