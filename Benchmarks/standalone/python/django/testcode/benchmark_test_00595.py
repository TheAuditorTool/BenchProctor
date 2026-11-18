# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00595(request):
    field_value = request.POST.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return JsonResponse({"saved": True})
