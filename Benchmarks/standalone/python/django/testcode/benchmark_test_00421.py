# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00421(request):
    field_value = request.POST.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return JsonResponse({"saved": True})
