# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def relay_value(value):
    return value

def BenchmarkTest53032(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = relay_value(forwarded_ip)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
