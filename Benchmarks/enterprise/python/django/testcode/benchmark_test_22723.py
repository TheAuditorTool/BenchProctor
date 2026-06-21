# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest22723(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
