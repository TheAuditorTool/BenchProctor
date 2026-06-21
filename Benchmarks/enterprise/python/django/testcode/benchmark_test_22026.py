# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest22026(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = normalise_input(host_value)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
