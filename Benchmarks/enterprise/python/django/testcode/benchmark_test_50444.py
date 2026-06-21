# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest50444(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = to_text(auth_header)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return JsonResponse({"saved": True})
