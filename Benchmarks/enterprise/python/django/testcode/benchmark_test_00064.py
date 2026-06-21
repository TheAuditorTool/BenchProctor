# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest00064(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = relay_value(forwarded_ip)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
